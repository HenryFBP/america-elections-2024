# America Elections 2024

# Running

1.  `poetry init; poetry shell`
2.  Create `.env` with this content:
    
    ```
    OPENAI_API_KEY=fillmeinplease
    FACEBOOK_ACCESS_TOKEN=fillmeinplease
    ```

3.  `poetry run src/test.py`

# Tech

https://ollama.ai/library/mistral
https://www.youtube.com/watch?v=XFiof0V3nhA
https://www.youtube.com/watch?v=yBI1nPep72Q

# Ideas

https://thehill.com/opinion/campaign/4162222-tracking-americas-freefall-down-the-rabbit-hole-of-toxic-politics/

An idea I just had about the 2024 election. I got tricked in 2020 into believing a lot of things that were false, and don't want others to go through it again.

I want to prevent the same political mania from occurring in the 2024 election by performing guerilla OSINT and showing people affected by propaganda the patterns in their behaviors, so they can avoid falling for the same traps.

- Find all of the Facebook posters that interacted with highly politicized content/memes during 2018, 2019, 2020.
- See if I can find trends in the posts/memes and group them by location
- See if I can find a way to track how extreme or inflammatory the posts that each person liked, and also track when those posts were posted, and what themes each had
- Build an inventory of communities and individuals that were negatively affected or influenced by Russian, Chinese, 4chan, or other propaganda during the 2020 elections
- Build a process to reach out to the individual humans that had their views influenced by propaganda, and tell them that their minds and views were hijacked by bad actors that want to see them tear their fellow US citizens apart, and that we shouldn't let the same thing happen in the 2024 election.
- Repeat until I've reached out to enough people to disrupt the cycle of divisive propaganda and give them enough meta-cognition to defend againt future propaganda attempts

Tech stack:

- Local AI agents for collecting and interpreting data
- NoSQL database for storing Posts, People, Locations (json)
- Selenium for browsing Facebook (probably want to use the API for this, but selenium would work)
- Python to glue it all together
