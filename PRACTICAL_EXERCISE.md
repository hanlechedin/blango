# Practical Exercise: Blog Post Analyzer

## Context
You are working on a blogging platform. The marketing team needs to analyze blog posts to understand content patterns and engagement. Your task is to implement a post analyzer and write tests for it.

## Requirements

### Part 1: Implement the PostAnalyzer class

Create a `post_analyzer.py` file with a `PostAnalyzer` class that can:

1. **Load posts from a JSON file** with the following structure:
```json
[
  {
    "id": 1,
    "title": "Getting Started with Python",
    "content": "Python is a great programming language...",
    "author": "john_doe",
    "tags": ["python", "tutorial", "beginners"],
    "published_date": "2024-01-15",
    "views": 1500,
    "likes": 45
  }
]
```

2. **Analyze posts** to provide:
   - Total number of posts
   - Average word count per post
   - Most common tags (top 5)
   - Author with most posts
   - Most viewed post
   - Engagement rate (likes/views ratio) for each post

3. **Filter posts** by:
   - Date range
   - Author
   - Minimum views
   - Tags (posts containing any of the specified tags)

### Part 2: Handle Edge Cases

Your implementation should handle:
- Empty files
- Invalid JSON format
- Missing required fields
- Posts with zero views (for engagement calculation)
- Invalid date formats

### Part 3: Write Tests

Create a `test_post_analyzer.py` file using PyTest that tests:

1. **Happy path scenarios**:
   - Loading valid data
   - Correct statistics calculation
   - Filtering works as expected

2. **Edge cases**:
   - Empty post list
   - Invalid data formats
   - Division by zero cases
   - Missing fields

3. **Integration scenarios**:
   - Loading from actual file
   - Multiple filters combined

## Time Allocation
- **35 minutes**: Implementation
- **5 minutes**: Discussion and questions

## What We're Looking For

### Code Quality
- Clear, readable code
- Appropriate use of Python features
- Good naming conventions
- Proper error handling

### Testing Approach
- Meaningful test cases
- Good use of PyTest features (fixtures, parametrize, etc.)
- Tests that actually verify behavior
- Edge case coverage

### Problem Solving
- How you break down the problem
- Your approach to handling edge cases
- How you debug when things don't work

### Communication
- Can you explain your thinking?
- Do you ask clarifying questions?
- Can you discuss trade-offs?

## Starter Code

You can start with this basic structure:

```python
# post_analyzer.py
import json
from typing import List, Dict, Optional
from datetime import datetime


class PostAnalyzer:
    def __init__(self, posts: List[Dict] = None):
        """Initialize with a list of post dictionaries."""
        self.posts = posts or []
    
    def load_from_file(self, filepath: str) -> None:
        """Load posts from a JSON file."""
        pass
    
    def get_total_posts(self) -> int:
        """Return the total number of posts."""
        pass
    
    def get_average_word_count(self) -> float:
        """Calculate average word count across all posts."""
        pass
    
    def get_most_common_tags(self, limit: int = 5) -> List[tuple]:
        """Return the most common tags with their counts."""
        pass
    
    def get_top_author(self) -> Optional[str]:
        """Return the author with the most posts."""
        pass
    
    def get_most_viewed_post(self) -> Optional[Dict]:
        """Return the post with the most views."""
        pass
    
    def calculate_engagement_rates(self) -> List[Dict]:
        """Calculate engagement rate (likes/views) for each post."""
        pass
    
    def filter_by_date_range(self, start_date: str, end_date: str) -> 'PostAnalyzer':
        """Filter posts by date range. Returns a new PostAnalyzer instance."""
        pass
    
    def filter_by_author(self, author: str) -> 'PostAnalyzer':
        """Filter posts by author. Returns a new PostAnalyzer instance."""
        pass
    
    def filter_by_min_views(self, min_views: int) -> 'PostAnalyzer':
        """Filter posts with at least min_views. Returns a new PostAnalyzer instance."""
        pass
    
    def filter_by_tags(self, tags: List[str]) -> 'PostAnalyzer':
        """Filter posts containing any of the specified tags."""
        pass
```

```python
# test_post_analyzer.py
import pytest
from post_analyzer import PostAnalyzer


# Add your tests here
def test_total_posts():
    """Test counting total posts."""
    pass


def test_average_word_count():
    """Test average word count calculation."""
    pass


# Add more tests...
```

## Sample Test Data

```python
SAMPLE_POSTS = [
    {
        "id": 1,
        "title": "Getting Started with Python",
        "content": "Python is a great programming language for beginners.",
        "author": "john_doe",
        "tags": ["python", "tutorial", "beginners"],
        "published_date": "2024-01-15",
        "views": 1500,
        "likes": 45
    },
    {
        "id": 2,
        "title": "Advanced Django Techniques",
        "content": "Django provides many advanced features for web development.",
        "author": "jane_smith",
        "tags": ["django", "python", "web"],
        "published_date": "2024-02-20",
        "views": 2000,
        "likes": 80
    },
    {
        "id": 3,
        "title": "Python for Data Science",
        "content": "Learn how to use Python for data analysis and machine learning.",
        "author": "john_doe",
        "tags": ["python", "data-science", "ml"],
        "published_date": "2024-03-10",
        "views": 3000,
        "likes": 120
    }
]
```

## Bonus Challenges (if time permits)

1. Add a method to find posts with similar content (using simple word matching)
2. Implement caching for expensive calculations
3. Add validation for post data structure
4. Support different date formats

## Discussion Points

After completing the exercise, be prepared to discuss:
- What design decisions did you make and why?
- What would you do differently if this were production code?
- How would you extend this for a real-world application?
- What performance considerations would you have for large datasets?
- How would you handle this if posts were stored in a database instead of a file?

## Tips

- **Don't aim for perfection** - we want to see your thought process
- **Ask questions** if requirements are unclear
- **Use the internet** - documentation lookup is encouraged
- **Think aloud** - share your reasoning
- **Focus on key features** - implement core functionality first
- **Write tests as you go** - or at least plan them
- **Handle errors gracefully** - but don't over-engineer

## Expected Deliverables

By the end of the exercise, you should have:
1. A working `PostAnalyzer` class with core functionality
2. Several PyTest test cases that pass
3. Basic error handling for edge cases
4. Clean, readable code

## Evaluation Criteria

We will assess:
- **Functionality** (30%): Does the code work and meet requirements?
- **Code Quality** (25%): Is the code clean, readable, and well-structured?
- **Testing** (25%): Are tests comprehensive and meaningful?
- **Problem Solving** (20%): How did you approach the problem?

Good luck! Remember, this is a collaborative exercise - feel free to ask questions and discuss your approach.
