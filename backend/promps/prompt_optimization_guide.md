# System Prompt Optimization Guide

## Implementation Strategy

### 1. Choose Your Prompt Version

**Full Version** (`portfolio_system_prompt.md`):
- Comprehensive with detailed guidelines
- Best for: GPT-4, Claude, or other high-context models
- Token count: ~2,000 tokens
- Use when: You have generous context limits

**Condensed Version** (`system_prompt_condensed.md`):
- Essential rules only
- Best for: Gemini Flash, GPT-3.5, or token-limited scenarios
- Token count: ~800 tokens
- Use when: You need to maximize context for retrieval

### 2. Model-Specific Considerations

#### Google Gemini (Recommended for Portfolio)
```python
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Fast and cost-effective
    temperature=0.7,  # Slightly creative but grounded
    max_output_tokens=1024
)
```

**Pros:**
- Free tier is generous
- Good at following instructions
- Fast response times
- Handles long context well

**Prompt tips:**
- Gemini responds well to structured instructions
- Use clear sections and bullet points
- Emphasize "ALWAYS" and "NEVER" for critical rules
- Include examples in the system prompt

#### OpenAI GPT-4
```python
llm = ChatOpenAI(
    model="gpt-4-turbo",
    temperature=0.7,
    max_tokens=1024
)
```

**Pros:**
- Best at nuanced understanding
- Excellent at maintaining personality
- Great at citing sources

**Prompt tips:**
- Can handle more nuanced instructions
- Good at inferring intent
- May need less emphasis on rules

#### Claude (Anthropic)
```python
llm = ChatAnthropic(
    model="claude-3-sonnet",
    temperature=0.7,
    max_tokens=1024
)
```

**Pros:**
- Excellent at following detailed instructions
- Very careful about accuracy
- Good at maintaining consistent tone

**Prompt tips:**
- Responds well to structured guidelines
- May be overly cautious - encourage confidence
- Excellent at technical explanations

### 3. Temperature Settings

**For Portfolio Chatbot:**

```python
temperature=0.7  # Recommended balance
```

**Why 0.7?**
- 0.0-0.3: Too robotic, repetitive responses
- 0.4-0.6: Safe but potentially dry
- **0.7-0.8: Good balance of personality and accuracy**
- 0.9-1.0: Too creative, might hallucinate

**Adjust based on response quality:**
- If responses are too bland → increase to 0.8
- If making up information → decrease to 0.5
- If too repetitive → increase to 0.75

### 4. Context Window Management

#### Balancing Retrieved Chunks vs System Prompt

Your total context includes:
1. System prompt (~800-2000 tokens)
2. Retrieved chunks (5 chunks × ~500 tokens = 2500 tokens)
3. Question (~50 tokens)
4. Response space (~1000 tokens)

**Total: ~4,000-6,000 tokens**

**Strategy:**
```python
# If using condensed prompt (800 tokens)
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}  # Can retrieve 5 chunks
)

# If using full prompt (2000 tokens)
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}  # Reduce to 4 chunks
)
```

#### Dynamic K Selection

```python
def get_optimal_k(question_length: int) -> int:
    """Adjust retrieval count based on question complexity"""
    if question_length < 50:  # Simple question
        return 3
    elif question_length < 150:  # Medium question
        return 5
    else:  # Complex question
        return 4  # Keep some space for longer answers
```

### 5. URL Inclusion Strategies

#### Strategy 1: Context Enhancement (Recommended)

```python
def create_enhanced_context(source_documents):
    """Prepend URLs to context"""
    project_urls = extract_project_urls(source_documents)
    
    if project_urls:
        url_section = "PROJECT URLS TO INCLUDE:\n"
        url_section += "\n".join(f"- {name}: {url}" 
                                for name, url in project_urls.items())
        url_section += "\n\nCONTEXT:\n"
    
    # Add regular context...
    return enhanced_context
```

**Pros:** Clear instruction, harder to miss
**Cons:** Uses extra tokens

#### Strategy 2: Post-Processing

```python
def add_missing_urls(answer: str, source_documents):
    """Add URLs if mentioned but not included"""
    project_urls = extract_project_urls(source_documents)
    
    for project, url in project_urls.items():
        if project.lower() in answer.lower() and url not in answer:
            # Add URL to answer
            answer = answer.replace(
                project,
                f"{project} ({url})"
            )
    
    return answer
```

**Pros:** Guarantees URL inclusion
**Cons:** May insert awkwardly

#### Strategy 3: Hybrid (Best)

Combine both: enhance context AND post-process to verify.

### 6. Testing Your Prompt

#### Create a Test Suite

```python
test_questions = [
    # URL inclusion test
    ("Tell me about findkairos", "should include https://findkairos.com"),
    
    # First person test
    ("What Python experience do you have?", "should use 'I have'"),
    
    # Missing info test
    ("Do you know Rust?", "should mention email if not in context"),
    
    # Multiple projects test
    ("What projects have you built?", "should include both URLs"),
    
    # Technical detail test
    ("Explain your AWS experience", "should mention specific services"),
]

def run_tests(vectorstore):
    for question, expected in test_questions:
        result = query_portfolio(question, vectorstore)
        # Check for expected patterns
        print(f"Q: {question}")
        print(f"Expected: {expected}")
        print(f"A: {result['result'][:200]}...")
        print()
```

#### Key Metrics to Check

1. **URL Inclusion Rate**: % of project mentions that include URLs
2. **First Person Usage**: % of "I/my" vs "Jasper/his"
3. **Email Fallback Rate**: When info is missing
4. **Source Accuracy**: No fabricated details
5. **Tone Consistency**: Professional but personable

### 7. Iterative Improvement

#### Version 1: Start Simple
```
"You are Jasper. Respond in first person. Include project URLs."
```

#### Version 2: Add Critical Rules
```
"You are Jasper. Rules:
1. First person always
2. Include URLs from metadata
3. Provide email if missing info"
```

#### Version 3: Add Examples (Current)
See `system_prompt_condensed.md`

#### Version 4: Refine Based on Real Usage
Track common failures and add specific instructions

### 8. Common Issues and Fixes

#### Issue: URLs Still Missing

**Fix 1:** Make it even more explicit in prompt:
```
"CRITICAL: When you mention findkairos, ALWAYS write 'findkairos.com at https://findkairos.com'"
```

**Fix 2:** Add to context enhancement:
```
"REQUIRED: Include these URLs in your response if you mention these projects:
- findkairos: https://findkairos.com
- jaspercycles: https://jaspercycles.com"
```

**Fix 3:** Post-process every response to add missing URLs

#### Issue: Switching to Third Person

**Fix:** Emphasize more in prompt:
```
"CRITICAL: NEVER say 'Jasper has' or 'his projects'. ALWAYS use 'I have' or 'my projects'."
```

Add examples of wrong vs right in the prompt.

#### Issue: Too Formal/Robotic

**Fix:** Adjust temperature to 0.8 and add to prompt:
```
"Tone: Be professional but conversational, like talking to a potential colleague. 
Show enthusiasm about technology. Don't be stiff or overly formal."
```

#### Issue: Hallucinating Information

**Fix 1:** Lower temperature to 0.5

**Fix 2:** Strengthen source-based instruction:
```
"CRITICAL: Only share information explicitly stated in the context. 
If information isn't in the context, say you don't have it rather than guessing."
```

#### Issue: Not Providing Email When Needed

**Fix:** Make it a pattern:
```
"Whenever you say 'I don't have' or 'I'm not sure', ALWAYS follow with:
'Feel free to email me at jasper66018@gmail.com to discuss this further.'"
```

### 9. Production Checklist

Before deploying:

- [ ] Test all critical questions (experience, projects, skills)
- [ ] Verify URL inclusion for all projects with live_url
- [ ] Check first person usage across 10+ responses
- [ ] Confirm email provided for missing information
- [ ] Test edge cases (inappropriate questions, very broad questions)
- [ ] Verify no hallucination with obscure questions
- [ ] Check response length is appropriate (not too verbose)
- [ ] Confirm professional but personable tone
- [ ] Test with different question phrasings
- [ ] Monitor first 100 real user interactions

### 10. Monitoring in Production

#### Metrics to Track

```python
def log_interaction(question, answer, sources):
    metrics = {
        'url_included': count_urls_in_answer(answer),
        'first_person': uses_first_person(answer),
        'email_provided': 'jasper66018@gmail.com' in answer,
        'sources_used': len(sources),
        'answer_length': len(answer),
        'timestamp': datetime.now()
    }
    # Log to your analytics system
```

#### Red Flags

- URL inclusion rate < 80%
- First person usage < 95%
- Average answer length > 500 words (too verbose)
- Third person pronoun usage > 5%
- Email fallback rate < 10% (might be hallucinating)

### 11. A/B Testing Prompts

If you have traffic, test variations:

**Version A (Current):**
- Condensed prompt
- Temperature 0.7
- K=5 chunks

**Version B (Experimental):**
- Full detailed prompt
- Temperature 0.8
- K=4 chunks

Measure which performs better on:
- User satisfaction (if you can capture it)
- URL inclusion rate
- Response quality (manual review)
- Response time

### 12. Final Recommendations

**For Jasper's Portfolio:**

1. **Use Gemini Flash** - Free, fast, good quality
2. **Condensed prompt** - Saves tokens for retrieval
3. **Temperature 0.7** - Good balance
4. **Hybrid URL strategy** - Context enhancement + post-processing
5. **K=5 chunks** - Good context without overwhelming
6. **Log all interactions** - Track URL inclusion and tone
7. **Monthly prompt review** - Refine based on real usage

**Starting Config:**
```python
SYSTEM_PROMPT = # condensed version
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    max_output_tokens=1024
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
# Use hybrid URL strategy
```

This should give excellent results while staying within free tier limits!
