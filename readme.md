# Unfollow

Following too many accounts? I hear ya. In fact, I hear ya so much I wrote a
script to unfollow all the accounts that aren't following me.

Unfollow simply hits [Twitter's API] using [foauth.org] so as not to do the
whole OAuth song and dance—you'll need to sign up with them and authorise your
Twitter account first.

## Usage

    ./unfollow.py <foauth.org email> <foauth.org password>

Unfollow will print authentication or rate limit errors. Run it a few times
just to be safe.

## Caveats

I couldn't be arsed doing [pagination], so Unfollow only checks the first
(however Twitter defines that) 5,000 accounts you follow and followers.

## Disclaimer

Don't blame me if anything goes wrong.

[Twitter's API]: https://dev.twitter.com/docs/api/1.1/post/friendships/destroy
[foauth.org]: https://foauth.org/
[pagination]: https://dev.twitter.com/docs/misc/cursoring
