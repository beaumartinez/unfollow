#! /usr/bin/env python

from sys import argv, exit

from requests_foauth import Foauth
from requests import Session

if __name__ == '__main__':
    try:
        email, password = argv[1], argv[2]
    except IndexError:
        print 'Usage: unfollow.py <foauth.org email> <foauth.org password>'

        exit(1)

    foauth = Foauth(email, password)

    session = Session()
    session.mount('https://', foauth)

    followers_response = session.get('https://api.twitter.com/1.1/followers/ids.json')

    followers = followers_response.json() 
    followers = followers['ids']
    followers = frozenset(followers)

    following_response = session.get('https://api.twitter.com/1.1/friends/ids.json')

    following = following_response.json() 
    following = following['ids']
    following = frozenset(following)

    to_unfollow = following - followers

    for user in to_unfollow:
        unfollow_response = session.post('https://api.twitter.com/1.1/friendships/destroy.json', {
            'user_id': user,
        })

        if unfollow_response.status_code != 200:
            print unfollow_response.status_code, unfollow_response.text

    # Sanity check. If we've unfollowed anyone we shouldn't have, follow them
    # again

    following_response = session.get('https://api.twitter.com/1.1/friends/ids.json')

    following = following_response.json() 
    following = following['ids']
    following = frozenset(following)

    to_follow = followers - following

    for user in to_follow:
        follow_response = session.post('https://api.twitter.com/1.1/friendships/create.json', {
            'user_id': user,
        })

        if follow_response.status_code != 200:
            print follow_response.status_code, follow_response.text
