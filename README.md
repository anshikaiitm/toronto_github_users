Toronto GitHub Users Data Analysis

This repository contains data on GitHub users based in Toronto who have over 100 followers, along with details about their public repositories. The project involves analyzing user profiles and repository information to uncover trends that could guide developers in building a stronger presence on GitHub.

Summary

1.Data Collection: Data was scraped using the GitHub API, focusing on user profiles in Toronto with over 100 followers. The data was stored in users.csv and repositories.csv files, capturing detailed user and repository metrics.

2.Findings: A key insight from the analysis is the limited correlation between the word count of a user's bio and their follower count. While bio content might add context, other factors seem more influential in attracting followers.

3.Recommendation: Developers looking to grow their followers on GitHub should focus on quality contributions and engaging repositories, as these likely play a more significant role than profile bios alone.

Files

users.csv: This file contains information about each user, including:

login: GitHub user ID,
name: Full name,
company: Workplace, cleaned and standardized to uppercase,
location: User location, focused on Toronto-based users,
email: Contact email,
hireable: Whether the user is open to hiring opportunities (formatted in lowercase),
bio: A brief description of the user,
public_repos, followers, following: Public repository count, follower count, and following count,
created_at: Account creation date.

repositories.csv: Contains each user's public repository information:

login: GitHub user ID (owner of the repository),
full_name: Repository name,
created_at: Repository creation date,
stargazers_count, watchers_count: Count of stars and watchers,
language: Main language of the repository,
has_projects, has_wiki: Boolean values indicating project and wiki features (formatted in lowercase),
license_name: Repository license.

README.md: Overview of the project, findings, and recommendations.

Code(gitscrap.py and analysis.py): The Python code used to scrape the data and run analyses is included to allow reproducibility and further exploration.

Code for project questions(1 to 16):Codes written to answer the questions asked in the project.

Methodology

Data Scraping: A Python script was used to interact with the GitHub API, pulling data for users meeting the location and follower criteria. Each user’s public repositories were retrieved and saved, with adjustments made to standardize formatting for ease of analysis.

Data Cleaning: Company names were stripped of leading @ symbols and converted to uppercase. Boolean fields such as hireable, has_projects, and has_wiki were standardized to lowercase (true, false).

Analysis: The project includes a basic regression analysis to explore the relationship between bio word count and follower count. Despite a common assumption that longer bios may attract more followers, results indicated a weak correlation.

Further Analysis and Insights

Follower Growth: While bio length does not strongly correlate with follower count, further analyses could examine how other factors, such as repository star count or collaboration activity, affect followers.

Project Setup: To replicate this analysis, run the scraping script with your own GitHub token, ensuring data retrieval and storage in the specified CSV formats.
