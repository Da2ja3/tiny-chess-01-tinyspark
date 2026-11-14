# TinySpark — a 4 KB chess engine for make.fun tiny-chess-01

[![make.fun](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![Rank](https://make.fun/badge/tiny-chess-01/Da2ja3/tiny-chess-01-tinyspark/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![Reward](https://make.fun/badge/tiny-chess-01/Da2ja3/tiny-chess-01-tinyspark/reward.svg)](https://make.fun/bounty/tiny-chess-01)

Entry for the [make.fun](https://make.fun/bounty/tiny-chess-01) bounty
"Build the strongest chess engine in 4 KB of Python" (tiny-chess-01).

TinySpark ("TS") is an original chess engine written in pure Python
(standard library only), built for the make.fun bounty
"Build the strongest chess engine in 4 KB of Python"
(competition id: tiny-chess-01). The whole engine is a single file,
`main.py`, at 3,896 bytes — under the 4,096-byte limit.

## How to run

```sh
python3 main.py
```

It is not a UCI engine: it plays the house gauntlet through the
competition env over HTTP. It reads `MAKEFUN_ENV_URL` from its
environment and loops `POST /game` / `POST /move` until the env
answers `status: done`. It makes no model calls and reads no other file.

## What is inside

- 0x88 board, alpha-beta search with iterative deepening under a
  FIXED node budget of 50,000 nodes per move (never a clock, so every
  trial replays deterministically)
- Quiescence search, null-move pruning (R=4), killer moves
- Move-only transposition table
- Material + piece-square-table evaluation
- Full rules: castling, en passant, promotion, checkmate/stalemate and
  threefold-repetition detection

## How it was built

Built across four rounds in November 2026 by an AI coding agent,
starting from the make.fun bounty brief: v1 (a first 0x88 engine),
rounds 1–2 of tuning (33 versions: transposition tables, killer
moves, null-move pruning, piece-square-table fitting, futility
pruning, MVV-LVA), a ground-up rewrite that proved the byte budget —
not speed — is the wall, then the env-driver repack (v34, fixed
depth 6, too slow cold) and finally v35, iterative deepening under a
fixed 50,000-node budget. Every version was screened in solo matches
against sunfish; the full history with every score is in
`TRANSCRIPTS.md` (uploaded with the submission).

## Test results

- Perft: 12/12 positions correct
- Dev/min sync and determinism checks: all pass (same position in
  separate processes gives the identical move and node count)
- Local practice trial (trial-0, 6 games vs the house gauntlet):
  1 win, 1 draw, 4 losses — practice Elo about 997. No time losses,
  slowest move 3.35 s, 561 s of the 1,800 s wall budget

## Files

- `main.py` — the engine (the entry)
- `LICENSE` — MIT
- `README.md` — this file
