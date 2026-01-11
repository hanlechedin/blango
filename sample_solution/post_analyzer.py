"""
Sample Solution for Post Analyzer Exercise
This is a reference implementation for interviewers.
"""

import json
from typing import List, Dict, Optional, Tuple
from datetime import datetime
from collections import Counter


class PostAnalyzer:
    """Analyzes blog posts to provide statistics and filtering capabilities."""
    
    def __init__(self, posts: List[Dict] = None):
        """Initialize with a list of post dictionaries."""
        self.posts = posts or []
    
    def load_from_file(self, filepath: str) -> None:
        """Load posts from a JSON file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.posts = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")
    
    def get_total_posts(self) -> int:
        """Return the total number of posts."""
        return len(self.posts)
    
    def get_average_word_count(self) -> float:
        """Calculate average word count across all posts."""
        if not self.posts:
            return 0.0
        
        total_words = 0
        for post in self.posts:
            content = post.get('content', '')
            words = content.split()
            total_words += len(words)
        
        return total_words / len(self.posts)
    
    def get_most_common_tags(self, limit: int = 5) -> List[Tuple[str, int]]:
        """Return the most common tags with their counts."""
        tag_counter = Counter()
        
        for post in self.posts:
            tags = post.get('tags', [])
            tag_counter.update(tags)
        
        return tag_counter.most_common(limit)
    
    def get_top_author(self) -> Optional[str]:
        """Return the author with the most posts."""
        if not self.posts:
            return None
        
        author_counter = Counter()
        for post in self.posts:
            author = post.get('author')
            if author:
                author_counter[author] += 1
        
        if not author_counter:
            return None
        
        return author_counter.most_common(1)[0][0]
    
    def get_most_viewed_post(self) -> Optional[Dict]:
        """Return the post with the most views."""
        if not self.posts:
            return None
        
        return max(self.posts, key=lambda p: p.get('views', 0))
    
    def calculate_engagement_rates(self) -> List[Dict]:
        """Calculate engagement rate (likes/views) for each post."""
        results = []
        
        for post in self.posts:
            views = post.get('views', 0)
            likes = post.get('likes', 0)
            
            # Handle division by zero
            engagement_rate = (likes / views * 100) if views > 0 else 0.0
            
            results.append({
                'id': post.get('id'),
                'title': post.get('title'),
                'engagement_rate': round(engagement_rate, 2)
            })
        
        return results
    
    def filter_by_date_range(self, start_date: str, end_date: str) -> 'PostAnalyzer':
        """Filter posts by date range. Returns a new PostAnalyzer instance."""
        try:
            start = datetime.fromisoformat(start_date)
            end = datetime.fromisoformat(end_date)
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")
        
        filtered_posts = []
        for post in self.posts:
            published_date_str = post.get('published_date')
            if published_date_str:
                try:
                    published_date = datetime.fromisoformat(published_date_str)
                    if start <= published_date <= end:
                        filtered_posts.append(post)
                except ValueError:
                    # Skip posts with invalid date format
                    continue
        
        return PostAnalyzer(filtered_posts)
    
    def filter_by_author(self, author: str) -> 'PostAnalyzer':
        """Filter posts by author. Returns a new PostAnalyzer instance."""
        filtered_posts = [
            post for post in self.posts 
            if post.get('author') == author
        ]
        return PostAnalyzer(filtered_posts)
    
    def filter_by_min_views(self, min_views: int) -> 'PostAnalyzer':
        """Filter posts with at least min_views. Returns a new PostAnalyzer instance."""
        filtered_posts = [
            post for post in self.posts 
            if post.get('views', 0) >= min_views
        ]
        return PostAnalyzer(filtered_posts)
    
    def filter_by_tags(self, tags: List[str]) -> 'PostAnalyzer':
        """Filter posts containing any of the specified tags."""
        filtered_posts = []
        for post in self.posts:
            post_tags = post.get('tags', [])
            # Check if any of the specified tags are in the post's tags
            if any(tag in post_tags for tag in tags):
                filtered_posts.append(post)
        
        return PostAnalyzer(filtered_posts)


# Sample data for testing
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
