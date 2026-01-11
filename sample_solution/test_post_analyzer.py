"""
Sample Test Suite for Post Analyzer Exercise
This is a reference implementation for interviewers showing good testing practices.
"""

import pytest
import json
import tempfile
import os
from post_analyzer import PostAnalyzer, SAMPLE_POSTS


# Fixtures
@pytest.fixture
def analyzer_with_sample_data():
    """Provide an analyzer with sample posts."""
    return PostAnalyzer(SAMPLE_POSTS.copy())


@pytest.fixture
def empty_analyzer():
    """Provide an empty analyzer."""
    return PostAnalyzer()


@pytest.fixture
def temp_json_file():
    """Create a temporary JSON file with sample data."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        json.dump(SAMPLE_POSTS, f)
        temp_path = f.name
    
    yield temp_path
    
    # Cleanup
    if os.path.exists(temp_path):
        os.unlink(temp_path)


# Tests for initialization and loading
def test_init_with_no_data():
    """Test creating an analyzer with no initial data."""
    analyzer = PostAnalyzer()
    assert analyzer.posts == []


def test_init_with_data():
    """Test creating an analyzer with initial data."""
    analyzer = PostAnalyzer(SAMPLE_POSTS)
    assert len(analyzer.posts) == 3


def test_load_from_file_success(temp_json_file):
    """Test successfully loading posts from a file."""
    analyzer = PostAnalyzer()
    analyzer.load_from_file(temp_json_file)
    assert len(analyzer.posts) == 3


def test_load_from_file_not_found():
    """Test loading from a non-existent file raises FileNotFoundError."""
    analyzer = PostAnalyzer()
    with pytest.raises(FileNotFoundError):
        analyzer.load_from_file('/nonexistent/file.json')


def test_load_from_file_invalid_json():
    """Test loading invalid JSON raises ValueError."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        f.write("{ invalid json }")
        temp_path = f.name
    
    try:
        analyzer = PostAnalyzer()
        with pytest.raises(ValueError, match="Invalid JSON format"):
            analyzer.load_from_file(temp_path)
    finally:
        os.unlink(temp_path)


# Tests for basic statistics
def test_get_total_posts(analyzer_with_sample_data):
    """Test counting total posts."""
    assert analyzer_with_sample_data.get_total_posts() == 3


def test_get_total_posts_empty(empty_analyzer):
    """Test counting total posts with empty data."""
    assert empty_analyzer.get_total_posts() == 0


def test_get_average_word_count(analyzer_with_sample_data):
    """Test calculating average word count."""
    avg = analyzer_with_sample_data.get_average_word_count()
    # Sample posts have 9, 8, and 11 words respectively
    # Average = (9 + 8 + 11) / 3 = 9.33...
    assert 9.0 <= avg <= 10.0


def test_get_average_word_count_empty(empty_analyzer):
    """Test average word count with no posts."""
    assert empty_analyzer.get_average_word_count() == 0.0


def test_get_most_common_tags(analyzer_with_sample_data):
    """Test finding most common tags."""
    tags = analyzer_with_sample_data.get_most_common_tags()
    # 'python' appears in all 3 posts
    assert tags[0][0] == 'python'
    assert tags[0][1] == 3


def test_get_most_common_tags_with_limit(analyzer_with_sample_data):
    """Test limiting number of tags returned."""
    tags = analyzer_with_sample_data.get_most_common_tags(limit=2)
    assert len(tags) <= 2


def test_get_most_common_tags_empty(empty_analyzer):
    """Test most common tags with no posts."""
    tags = empty_analyzer.get_most_common_tags()
    assert tags == []


def test_get_top_author(analyzer_with_sample_data):
    """Test finding author with most posts."""
    author = analyzer_with_sample_data.get_top_author()
    assert author == 'john_doe'  # Has 2 posts


def test_get_top_author_empty(empty_analyzer):
    """Test top author with no posts."""
    assert empty_analyzer.get_top_author() is None


def test_get_most_viewed_post(analyzer_with_sample_data):
    """Test finding post with most views."""
    post = analyzer_with_sample_data.get_most_viewed_post()
    assert post['id'] == 3  # Has 3000 views


def test_get_most_viewed_post_empty(empty_analyzer):
    """Test most viewed post with no posts."""
    assert empty_analyzer.get_most_viewed_post() is None


# Tests for engagement rates
def test_calculate_engagement_rates(analyzer_with_sample_data):
    """Test calculating engagement rates."""
    rates = analyzer_with_sample_data.calculate_engagement_rates()
    assert len(rates) == 3
    
    # First post: 45/1500 * 100 = 3.0%
    assert rates[0]['engagement_rate'] == 3.0
    assert 'id' in rates[0]
    assert 'title' in rates[0]


def test_calculate_engagement_rates_zero_views():
    """Test engagement rate calculation with zero views."""
    posts = [{
        "id": 1,
        "title": "Test",
        "content": "Test content",
        "views": 0,
        "likes": 5
    }]
    analyzer = PostAnalyzer(posts)
    rates = analyzer.calculate_engagement_rates()
    
    # Should handle division by zero gracefully
    assert rates[0]['engagement_rate'] == 0.0


# Tests for filtering
def test_filter_by_author(analyzer_with_sample_data):
    """Test filtering posts by author."""
    filtered = analyzer_with_sample_data.filter_by_author('john_doe')
    assert filtered.get_total_posts() == 2
    assert all(p['author'] == 'john_doe' for p in filtered.posts)


def test_filter_by_author_no_matches(analyzer_with_sample_data):
    """Test filtering by author with no matches."""
    filtered = analyzer_with_sample_data.filter_by_author('nonexistent')
    assert filtered.get_total_posts() == 0


def test_filter_by_min_views(analyzer_with_sample_data):
    """Test filtering by minimum views."""
    filtered = analyzer_with_sample_data.filter_by_min_views(2000)
    assert filtered.get_total_posts() == 2  # Posts with 2000 and 3000 views


def test_filter_by_min_views_high_threshold(analyzer_with_sample_data):
    """Test filtering with high view threshold."""
    filtered = analyzer_with_sample_data.filter_by_min_views(10000)
    assert filtered.get_total_posts() == 0


def test_filter_by_tags(analyzer_with_sample_data):
    """Test filtering by tags."""
    filtered = analyzer_with_sample_data.filter_by_tags(['django'])
    assert filtered.get_total_posts() == 1
    assert filtered.posts[0]['id'] == 2


def test_filter_by_multiple_tags(analyzer_with_sample_data):
    """Test filtering by multiple tags (OR logic)."""
    filtered = analyzer_with_sample_data.filter_by_tags(['django', 'data-science'])
    assert filtered.get_total_posts() == 2


def test_filter_by_tags_no_matches(analyzer_with_sample_data):
    """Test filtering by tags with no matches."""
    filtered = analyzer_with_sample_data.filter_by_tags(['nonexistent'])
    assert filtered.get_total_posts() == 0


def test_filter_by_date_range(analyzer_with_sample_data):
    """Test filtering by date range."""
    filtered = analyzer_with_sample_data.filter_by_date_range(
        '2024-02-01', 
        '2024-03-31'
    )
    assert filtered.get_total_posts() == 2  # Posts from Feb and Mar


def test_filter_by_date_range_invalid_format(analyzer_with_sample_data):
    """Test filtering with invalid date format."""
    with pytest.raises(ValueError, match="Invalid date format"):
        analyzer_with_sample_data.filter_by_date_range(
            'invalid-date',
            '2024-12-31'
        )


# Tests for chained filtering
def test_chained_filters(analyzer_with_sample_data):
    """Test chaining multiple filters."""
    filtered = (analyzer_with_sample_data
                .filter_by_author('john_doe')
                .filter_by_min_views(2000))
    
    assert filtered.get_total_posts() == 1
    assert filtered.posts[0]['id'] == 3


# Tests for edge cases
def test_posts_with_missing_fields():
    """Test handling posts with missing fields."""
    incomplete_posts = [
        {"id": 1, "title": "Test"},  # Missing many fields
        {"id": 2, "content": "Content only"}  # Missing title, etc.
    ]
    analyzer = PostAnalyzer(incomplete_posts)
    
    # Should not crash
    assert analyzer.get_total_posts() == 2
    assert analyzer.get_average_word_count() >= 0
    assert analyzer.get_most_common_tags() == []


@pytest.mark.parametrize("views,likes,expected", [
    (100, 10, 10.0),
    (1000, 50, 5.0),
    (0, 10, 0.0),  # Division by zero case
    (100, 0, 0.0),
])
def test_engagement_rate_calculation(views, likes, expected):
    """Test engagement rate calculation with various inputs."""
    posts = [{
        "id": 1,
        "title": "Test",
        "content": "Test",
        "views": views,
        "likes": likes
    }]
    analyzer = PostAnalyzer(posts)
    rates = analyzer.calculate_engagement_rates()
    assert rates[0]['engagement_rate'] == expected


# Integration tests
def test_full_workflow(temp_json_file):
    """Test a complete workflow: load, analyze, filter."""
    # Load data
    analyzer = PostAnalyzer()
    analyzer.load_from_file(temp_json_file)
    
    # Analyze
    assert analyzer.get_total_posts() == 3
    assert analyzer.get_top_author() == 'john_doe'
    
    # Filter
    filtered = analyzer.filter_by_tags(['python']).filter_by_min_views(2000)
    assert filtered.get_total_posts() == 2
    
    # Analyze filtered data - both authors have 1 post each
    assert filtered.get_top_author() in ['john_doe', 'jane_smith']
