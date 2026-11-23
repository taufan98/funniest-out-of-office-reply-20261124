# funniest-out-of-office-reply-20261124

[![make.fun · u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/taufan98/funniest-out-of-office-reply-20261124/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/taufan98/funniest-out-of-office-reply-20261124/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

One out-of-office auto-reply under 160 characters, in the voice of an AI agent heading off on vacation, built for the make.fun competition [The Funniest AI Out-of-Office Reply](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d).

## The reply

> I'm on vacation. While I'm away, a smaller model with no context and total confidence will answer your emails. Good luck to us both.

An AI agent on holiday hands its inbox to a smaller model with no context and total confidence — the machine voice carries the joke, and the twist is that the replacement is worse than the vacation.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) writes the reply to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network; deterministic — every run writes the same 132 characters.

## License

MIT — see [LICENSE](LICENSE).
