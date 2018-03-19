# two-player-card-game
Python implementation of [this](https://dev.to/mortoray/interview-question-a-two-player-card-game-67i) cool interview question

# Introduction

When i started to read this post, i really liked and decided to first try to implement and then finish to read (this because the post is about some insights and the way some interviewed do it the implementation)

# Enunciation (copied from [this post](https://dev.to/mortoray/interview-question-a-two-player-card-game-67i) on dev.to)

## Two Player Card Game
Here is the description of the game simulation.

- this is a two player card game
- the game starts with a deck of cards
- the cards are dealt out to both players
- on each turn:
- both players turn over their top-most card
- the player with the higher valued card takes the cards 
and puts them in their scoring pile (scoring 1 point per card)
- this continues until the players have no cards left
- the player with the highest score wins

# Implementation

## Doubts

- No suits is used?
- What do with draw game?

## Deductions

- Because of suits can have same value, use only numbers
- Use fourteen numbered cards, not thirteen, to keep with pair hands
- All cards are dealt out on the first turn only because the instruction is before "on each turn" line
- Each turn a player will receive two point for the two cards they catch
