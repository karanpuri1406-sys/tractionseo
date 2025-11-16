// TractionSEO - Main JavaScript File

// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('nav ul');
    
    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }

    // Smooth Scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Email Form Submission
    const emailForms = document.querySelectorAll('.email-form');
    emailForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            handleEmailSignup(email, this);
        });
    });

    // Coaching Form Submission
    const coachingForm = document.getElementById('coaching-form');
    if (coachingForm) {
        coachingForm.addEventListener('submit', function(e) {
            e.preventDefault();
            handleCoachingSubmission(this);
        });
    }

    // Glossary Search
    const glossarySearch = document.getElementById('glossary-search');
    if (glossarySearch) {
        glossarySearch.addEventListener('input', function() {
            filterGlossary(this.value);
        });
    }

    // Directory Filters
    const filterButtons = document.querySelectorAll('.filter-btn');
    filterButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            filterButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            filterDirectory(this.dataset.category);
        });
    });
});

// Email Signup Handler
function handleEmailSignup(email, form) {
    if (!validateEmail(email)) {
        showMessage(form, 'Please enter a valid email address', 'error');
        return;
    }

    const button = form.querySelector('button');
    const originalText = button.textContent;
    button.innerHTML = '<span class="loading"></span> Subscribing...';
    button.disabled = true;

    // Simulate API call
    setTimeout(() => {
        // In production, this would send to karanpuri1406@gmail.com
        console.log('Email signup:', email);
        showMessage(form, '🎉 Success! Check your email for the free toolkit.', 'success');
        form.reset();
        button.textContent = originalText;
        button.disabled = false;
    }, 1500);
}

// Coaching Form Handler
function handleCoachingSubmission(form) {
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    const button = form.querySelector('button[type="submit"]');
    const originalText = button.textContent;
    button.innerHTML = '<span class="loading"></span> Sending...';
    button.disabled = true;

    // Simulate sending email to karanpuri1406@gmail.com
    setTimeout(() => {
        console.log('Coaching inquiry:', data);
        
        // Create success message
        const successDiv = document.createElement('div');
        successDiv.className = 'success-message';
        successDiv.innerHTML = `
            <h3>🎉 Booking Request Received!</h3>
            <p>Thank you ${data.name}! We'll contact you at ${data.email} within 24 hours to schedule your coaching session.</p>
        `;
        
        form.parentNode.insertBefore(successDiv, form);
        form.style.display = 'none';
        
        button.textContent = originalText;
        button.disabled = false;
    }, 2000);
}

// Email Validation
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Show Message
function showMessage(element, message, type) {
    const messageDiv = document.createElement('div');
    messageDiv.className = type === 'success' ? 'success-message' : 'error-message';
    messageDiv.textContent = message;
    
    element.appendChild(messageDiv);
    
    setTimeout(() => {
        messageDiv.remove();
    }, 5000);
}

// Glossary Filter
function filterGlossary(searchTerm) {
    const items = document.querySelectorAll('.glossary-item');
    const term = searchTerm.toLowerCase();
    
    items.forEach(item => {
        const text = item.textContent.toLowerCase();
        if (text.includes(term)) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}

// Directory Filter
function filterDirectory(category) {
    const listings = document.querySelectorAll('.tool-listing');
    
    listings.forEach(listing => {
        if (category === 'all' || listing.dataset.category === category) {
            listing.style.display = 'flex';
        } else {
            listing.style.display = 'none';
        }
    });
}

// Keyword Difficulty Calculator
function calculateKeywordDifficulty() {
    const keyword = document.getElementById('keyword-input').value;
    const location = document.getElementById('location-select').value;
    
    if (!keyword) {
        alert('Please enter a keyword');
        return;
    }
    
    // Simulate calculation
    const difficulty = Math.floor(Math.random() * 100);
    const volume = Math.floor(Math.random() * 10000) + 100;
    const competition = difficulty > 70 ? 'High' : difficulty > 40 ? 'Medium' : 'Low';
    
    let difficultyLevel, recommendation;
    if (difficulty < 30) {
        difficultyLevel = 'Easy';
        recommendation = 'Great opportunity! This keyword is relatively easy to rank for.';
    } else if (difficulty < 60) {
        difficultyLevel = 'Medium';
        recommendation = 'Moderate competition. With good content and backlinks, you can rank.';
    } else {
        difficultyLevel = 'Hard';
        recommendation = 'High competition. Consider long-tail variations or build authority first.';
    }
    
    const resultHTML = `
        <h3>Results for "${keyword}" in ${location}</h3>
        <div class="score">${difficulty}</div>
        <div class="difficulty-badge difficulty-${difficultyLevel.toLowerCase()}">${difficultyLevel}</div>
        <p><strong>Estimated Monthly Searches:</strong> ${volume.toLocaleString()}</p>
        <p><strong>Competition Level:</strong> ${competition}</p>
        <p><strong>Recommendation:</strong> ${recommendation}</p>
        <button class="btn btn-primary mt-2" onclick="document.getElementById('email-capture-modal').style.display='block'">
            Get Detailed Report (Free)
        </button>
    `;
    
    document.getElementById('keyword-result').innerHTML = resultHTML;
}

// SEO ROI Calculator
function calculateROI() {
    const traffic = parseFloat(document.getElementById('current-traffic').value);
    const conversion = parseFloat(document.getElementById('conversion-rate').value);
    const orderValue = parseFloat(document.getElementById('order-value').value);
    
    if (!traffic || !conversion || !orderValue) {
        alert('Please fill in all fields');
        return;
    }
    
    const currentRevenue = traffic * (conversion / 100) * orderValue;
    const projectedTraffic = traffic * 3; // 3x increase
    const projectedRevenue = projectedTraffic * (conversion / 100) * orderValue;
    const increase = projectedRevenue - currentRevenue;
    
    const resultHTML = `
        <h3>Your SEO ROI Projection</h3>
        <p><strong>Current Monthly Revenue:</strong> ₹${currentRevenue.toLocaleString('en-IN')}</p>
        <p><strong>Projected Revenue (with SEO):</strong> ₹${projectedRevenue.toLocaleString('en-IN')}</p>
        <div class="score">+₹${increase.toLocaleString('en-IN')}</div>
        <p style="text-align: center; color: #10B981; font-weight: 600;">Potential Monthly Increase</p>
        <p><strong>Annual Potential:</strong> ₹${(increase * 12).toLocaleString('en-IN')}</p>
        <p style="margin-top: 1.5rem;"><strong>Investment Comparison:</strong></p>
        <p>• Paid Ads for same traffic: ₹${(projectedTraffic * 10).toLocaleString('en-IN')}/month</p>
        <p>• SEO Investment: ₹15,000-30,000/month (one-time effort, long-term results)</p>
        <button class="btn btn-orange mt-2" onclick="window.location.href='coaching.html'">
            Book Strategy Session
        </button>
    `;
    
    document.getElementById('roi-result').innerHTML = resultHTML;
}

// SEO Score Checker
function checkSEOScore() {
    const url = document.getElementById('website-url').value;
    
    if (!url) {
        alert('Please enter a website URL');
        return;
    }
    
    // Simulate checking
    const button = document.querySelector('#seo-checker-tool button');
    button.innerHTML = '<span class="loading"></span> Analyzing...';
    button.disabled = true;
    
    setTimeout(() => {
        const score = Math.floor(Math.random() * 40) + 50; // 50-90
        const issues = [
            'Missing meta descriptions on 3 pages',
            'Page load time: 4.2s (should be under 3s)',
            'Mobile usability issues detected',
            '12 broken links found',
            'Images missing alt text'
        ];
        
        const recommendations = [
            'Optimize images (use WebP format)',
            'Add meta descriptions to all pages',
            'Improve mobile responsiveness',
            'Fix broken links',
            'Add schema markup'
        ];
        
        const resultHTML = `
            <h3>SEO Score for ${url}</h3>
            <div class="score">${score}/100</div>
            <p style="text-align: center; font-weight: 600;">
                ${score > 80 ? 'Good!' : score > 60 ? 'Needs Improvement' : 'Critical Issues'}
            </p>
            <h4 style="margin-top: 2rem;">Issues Found:</h4>
            <ul style="margin-left: 1.5rem;">
                ${issues.map(issue => `<li>${issue}</li>`).join('')}
            </ul>
            <h4 style="margin-top: 1.5rem;">Recommendations:</h4>
            <ul style="margin-left: 1.5rem;">
                ${recommendations.map(rec => `<li>${rec}</li>`).join('')}
            </ul>
            <button class="btn btn-primary mt-2" onclick="window.location.href='guide.html'">
                Learn How to Fix These Issues
            </button>
        `;
        
        document.getElementById('seo-score-result').innerHTML = resultHTML;
        button.textContent = 'Check SEO Score';
        button.disabled = false;
    }, 3000);
}

// Generate AI Prompt
function generatePrompt() {
    const task = document.getElementById('prompt-task').value;
    
    const prompts = {
        keyword: `Act as an SEO expert. I need you to generate a comprehensive list of keywords for [YOUR TOPIC/NICHE].

Please provide:
1. 10 primary keywords (high volume, competitive)
2. 20 long-tail keywords (lower competition, specific intent)
3. 10 question-based keywords (what, how, why, when)
4. 5 local keywords (include city/region: [YOUR LOCATION])

For each keyword, estimate:
- Search intent (informational, commercial, transactional)
- Difficulty level (easy, medium, hard)
- Content type that would rank (blog, product page, video, etc.)

Format the output in a table for easy analysis.`,

        content: `Act as an SEO content strategist. Create a detailed content outline for: [YOUR KEYWORD/TOPIC]

Include:
1. SEO-optimized title (under 60 characters)
2. Meta description (under 160 characters)
3. H1 heading
4. 5-7 H2 subheadings with brief descriptions
5. Key points to cover under each section
6. LSI keywords to naturally include
7. Internal linking opportunities
8. External sources to reference
9. Call-to-action suggestions
10. Content length recommendation

Target audience: [YOUR AUDIENCE]
Content goal: [INFORM/CONVERT/ENGAGE]`,

        meta: `Act as an SEO copywriter. Create compelling meta descriptions for the following pages:

Page 1: [PAGE TITLE/TOPIC]
Page 2: [PAGE TITLE/TOPIC]
Page 3: [PAGE TITLE/TOPIC]

Requirements:
- Maximum 155 characters
- Include primary keyword naturally
- Add a clear call-to-action
- Create urgency or curiosity
- Match search intent
- Be unique for each page

Also suggest 3 alternative versions for A/B testing.`,

        competitor: `Act as an SEO analyst. Analyze the following competitor website: [COMPETITOR URL]

Provide insights on:
1. Top ranking keywords (estimate 10-15)
2. Content strategy (topics, format, frequency)
3. Backlink profile (quality, quantity, sources)
4. Technical SEO strengths
5. Content gaps we can exploit
6. Their unique value proposition
7. Social media presence
8. User experience elements
9. Conversion optimization tactics
10. Opportunities for us to outrank them

Format as an actionable report.`,

        local: `Act as a local SEO specialist. Create a local SEO strategy for:

Business: [YOUR BUSINESS NAME]
Location: [CITY, STATE]
Industry: [YOUR INDUSTRY]

Provide:
1. Google Business Profile optimization checklist
2. Local keyword targets (15-20 keywords)
3. Citation building strategy (top 20 directories)
4. Local content ideas (10 blog topics)
5. Review generation tactics
6. Local link building opportunities
7. Schema markup recommendations
8. Competitor analysis (top 3 local competitors)
9. NAP consistency audit plan
10. Local social media strategy

Include specific action items with priority levels.`
    };
    
    const resultHTML = `
        <h3>Generated Prompt for ${task.charAt(0).toUpperCase() + task.slice(1)}</h3>
        <div style="background: #F9FAFB; padding: 1.5rem; border-radius: 8px; margin-top: 1rem;">
            <pre style="white-space: pre-wrap; font-family: monospace; font-size: 0.9rem;">${prompts[task]}</pre>
        </div>
        <button class="btn btn-primary mt-2" onclick="copyPrompt()">
            📋 Copy Prompt
        </button>
        <p style="margin-top: 1rem; font-size: 0.9rem; color: #6B7280;">
            <strong>How to use:</strong> Copy this prompt, paste it into ChatGPT or Claude, and replace the bracketed placeholders with your specific information.
        </p>
    `;
    
    document.getElementById('prompt-result').innerHTML = resultHTML;
}

// Copy Prompt to Clipboard
function copyPrompt() {
    const promptText = document.querySelector('#prompt-result pre').textContent;
    navigator.clipboard.writeText(promptText).then(() => {
        alert('✅ Prompt copied to clipboard!');
    });
}

// Local SEO Quiz
let quizAnswers = {};

function startQuiz() {
    document.getElementById('quiz-intro').style.display = 'none';
    document.getElementById('quiz-questions').style.display = 'block';
}

function submitQuiz() {
    const form = document.getElementById('local-seo-quiz');
    const formData = new FormData(form);
    
    let score = 0;
    formData.forEach((value, key) => {
        quizAnswers[key] = value;
        if (value === 'yes') score++;
    });
    
    const totalQuestions = 10;
    const percentage = (score / totalQuestions) * 100;
    
    let assessment, recommendations;
    
    if (percentage >= 80) {
        assessment = "Excellent! Your local SEO foundation is strong.";
        recommendations = [
            "Focus on advanced tactics like local link building",
            "Create location-specific landing pages",
            "Implement advanced schema markup",
            "Build relationships with local influencers"
        ];
    } else if (percentage >= 50) {
        assessment = "Good start, but there's room for improvement.";
        recommendations = [
            "Optimize your Google Business Profile completely",
            "Build citations on top local directories",
            "Create location-specific content",
            "Encourage and respond to customer reviews",
            "Ensure NAP consistency across all platforms"
        ];
    } else {
        assessment = "Your local SEO needs immediate attention!";
        recommendations = [
            "Claim and verify your Google Business Profile",
            "Add complete business information (hours, photos, services)",
            "Start collecting customer reviews",
            "Create location pages on your website",
            "Build basic citations (Google, Facebook, Yelp)",
            "Optimize for local keywords",
            "Add local schema markup to your website"
        ];
    }
    
    const resultHTML = `
        <h3>Your Local SEO Score</h3>
        <div class="score">${percentage.toFixed(0)}%</div>
        <p style="text-align: center; font-weight: 600; font-size: 1.1rem;">${assessment}</p>
        
        <h4 style="margin-top: 2rem;">Personalized Action Plan:</h4>
        <ul style="margin-left: 1.5rem; margin-top: 1rem;">
            ${recommendations.map(rec => `<li style="margin-bottom: 0.5rem;">${rec}</li>`).join('')}
        </ul>
        
        <div style="margin-top: 2rem; padding: 1.5rem; background: linear-gradient(135deg, #9333EA 0%, #2563EB 100%); border-radius: 8px; color: white; text-align: center;">
            <h4 style="color: white; margin-bottom: 1rem;">Want a Custom Local SEO Strategy?</h4>
            <p>Get personalized coaching to dominate local search in your area.</p>
            <button class="btn btn-primary mt-1" onclick="window.location.href='coaching.html'" style="background: white; color: #2563EB;">
                Book 1-on-1 Coaching
            </button>
        </div>
    `;
    
    document.getElementById('quiz-questions').style.display = 'none';
    document.getElementById('quiz-result').innerHTML = resultHTML;
    document.getElementById('quiz-result').style.display = 'block';
}