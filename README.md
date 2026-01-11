# blango

Starting point for the Advanced Django course. This is the equivalent of the following command:

```bash
$ django-admin.py startproject blango
```

---

## Interview Materials

This repository now includes comprehensive materials for conducting technical interviews. These materials are designed for a second-phase interview process and are conducted in English.

### 📚 Available Documents

#### 1. **[INTERVIEW_STRUCTURE.md](INTERVIEW_STRUCTURE.md)**
The main interview guide containing:
- Complete interview structure and timeline
- Practical exercise format and objectives
- Technical discussion topics covering:
  - Software Architecture & Design Patterns
  - Django & Python
  - Cloud Technologies & DevOps
  - Testing & Quality Assurance
  - Database Design
  - Security
  - Collaboration & Soft Skills
- Evaluation rubric and criteria
- Tips for interviewers

#### 2. **[PRACTICAL_EXERCISE.md](PRACTICAL_EXERCISE.md)**
A ready-to-use practical coding exercise:
- **Task**: Build a Blog Post Analyzer
- **Technologies**: Python (no frameworks) + PyTest
- **Duration**: 35-40 minutes
- **Skills Assessed**: 
  - Code quality and structure
  - Problem-solving approach
  - Testing mindset
  - Error handling
- Includes starter code and sample data

#### 3. **[TECHNICAL_DISCUSSION_GUIDE.md](TECHNICAL_DISCUSSION_GUIDE.md)**
Quick reference for conducting technical discussions:
- Key questions for each topic area
- What to listen for in responses
- Follow-up question suggestions
- Interview tips and best practices
- Decision-making framework

#### 4. **[sample_solution/](sample_solution/)**
Reference implementation for interviewers:
- Complete, working solution
- Comprehensive test suite (34 tests)
- Best practices demonstration
- README with guidance

### 🎯 Interview Format

**Part 1: Practical Exercise (45 min)**
- Live coding session with screen sharing
- Candidate implements a Python analyzer class
- Write PyTest tests
- Focus on problem-solving and communication

**Part 2: Technical Discussion (30 min)**
- Informal, conversational format
- 2-3 topic areas based on role requirements
- Real-world scenarios and experiences
- Architecture, Django, or cloud technologies

### 🚀 Quick Start for Interviewers

1. **Prepare** (before interview):
   - Review [INTERVIEW_STRUCTURE.md](INTERVIEW_STRUCTURE.md)
   - Read the [PRACTICAL_EXERCISE.md](PRACTICAL_EXERCISE.md)
   - Familiarize yourself with [sample_solution/](sample_solution/)
   - Choose 2-3 technical discussion topics

2. **During Interview**:
   - Share the practical exercise requirements
   - Encourage thinking aloud
   - Use [TECHNICAL_DISCUSSION_GUIDE.md](TECHNICAL_DISCUSSION_GUIDE.md) for reference
   - Take notes on candidate responses

3. **After Interview**:
   - Complete evaluation rubric
   - Write detailed feedback
   - Discuss with team

### ✅ Testing the Sample Solution

```bash
cd sample_solution

# Install pytest
pip install pytest

# Run all tests
pytest test_post_analyzer.py -v

# Run with coverage
pip install pytest-cov
pytest test_post_analyzer.py --cov=post_analyzer --cov-report=term-missing
```

### 📋 Key Features

- ✅ **Comprehensive**: Covers all aspects of the interview
- ✅ **Ready-to-use**: No additional preparation needed
- ✅ **Flexible**: Adapt to different seniority levels
- ✅ **Fair**: Consistent evaluation criteria
- ✅ **Practical**: Focus on real-world skills
- ✅ **Well-tested**: Sample solution with 34 passing tests

### 🎓 What We Assess

**Technical Skills (80%)**:
- Code quality and structure (10%)
- Problem-solving ability (10%)
- Testing practices (10%)
- Technical depth (15%)
- Experience with relevant technologies (10%)
- Architecture thinking (10%)
- Learning mindset (5%)

**Soft Skills (20%)**:
- Communication clarity (10%)
- Collaboration approach (10%)

### 📝 Notes

- All interview content is in **English**
- Materials are suitable for mid to senior-level positions
- Adapt difficulty based on candidate's experience
- Focus on thought process over perfect solutions
- Create a comfortable, collaborative atmosphere

---

## Django Project

The rest of this README pertains to the Django project structure...
