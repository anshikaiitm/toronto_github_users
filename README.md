# Toronto GitHub Users Data Analysis

- **Data Collection**: This project scraped user and repository data of GitHub users located in Toronto with over 100 followers using the GitHub API.
- **Key Insight**: Certain companies, like GarnerCorp and Shopify, show a high volume of public GitHub contributions, while niche languages like Cython and Forth exhibit higher engagement rates.
- **Recommendation**: Developers can increase visibility by contributing to popular, highly engaged languages or open-source projects associated with influential companies.

---

### Project Overview
This project aims to analyze GitHub data for Toronto-based users with significant followings. We scraped user and repository data, focusing on engagement metrics, to draw insights on popular languages, active companies, and engagement trends in Toronto’s GitHub community.

### Key Findings

#### 1. Top Contributors by Company
The companies with the highest volume of public contributions among Toronto’s GitHub users are:
- **GarnerCorp**: 2,085 repositories
- **Shopify**: 1,455 repositories
- **Quinntyne**: 1,216 repositories

These companies have established strong open-source profiles, suggesting active engagement within the GitHub community. 

#### 2. Languages with Highest Engagement
Languages associated with the highest levels of engagement (based on average stargazers and watchers per repository) include:
- **Cython**: Avg. 1,780 stargazers, 1,780 watchers across 6 repositories
- **Forth**: Avg. 1,192 stargazers, 1,192 watchers for 1 repository
- **ASP.NET**: Avg. 414 stargazers, 414 watchers across 2 repositories
- **BrighterScript**: Avg. 313 stargazers, 313 watchers for 1 repository
- **SAS**: Avg. 172 stargazers, 172 watchers for 1 repository

These findings reveal that languages with niche or specialized applications, like Cython and Forth, show high per-repo engagement, possibly due to targeted, high-value applications or the specialized knowledge required to contribute.

### Actionable Insights

1. **Leverage High-Engagement Languages**: Developers seeking visibility could benefit by contributing to repositories using high-engagement languages like Cython and Forth, as they attract more attention relative to other languages.
2. **Explore Popular Companies’ Open-Source Projects**: Engaging with repositories associated with high-contributing companies, such as GarnerCorp and Shopify, can enhance developers’ profiles and networking opportunities within active open-source communities.

---

### File Structure

- **`users.csv`**: Contains details on Toronto-based GitHub users with the following fields:
  - `login`, `name`, `company`, `location`, `bio`, `public_repos`, `followers`, `following`, `created_at`
- **`repositories.csv`**: Contains details on public repositories, with fields:
  - `full_name`, `created_at`, `stargazers_count`, `watchers_count`, `language`, `has_projects`, `has_wiki`, `license_name`

---

### How to Use

1. Clone the repository.
2. Open `users.csv` and `repositories.csv` to analyze Toronto’s GitHub community, explore active companies, and identify high-engagement languages.
