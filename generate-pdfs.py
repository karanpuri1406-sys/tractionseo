#!/usr/bin/env python3
"""
Generate 3 beautiful, well-researched SEO resource PDFs for TractionSEO
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, ListFlowable, ListItem
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
import os

# TractionSEO Brand Colors
BLUE = HexColor('#2563EB')
PURPLE = HexColor('#9333EA')
ORANGE = HexColor('#F97316')
DARK_GRAY = HexColor('#1F2937')
LIGHT_GRAY = HexColor('#6B7280')

def create_header_footer(canvas, doc):
    """Add header and footer to each page"""
    canvas.saveState()
    
    # Footer
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(LIGHT_GRAY)
    canvas.drawString(inch, 0.5 * inch, "TractionSEO © 2025")
    canvas.drawRightString(7.5 * inch, 0.5 * inch, f"Page {doc.page}")
    canvas.drawCentredString(4.25 * inch, 0.5 * inch, "karanpuri1406@gmail.com")
    
    canvas.restoreState()

# ============================================================================
# PDF 1: 100-Point SEO Audit Checklist
# ============================================================================

def create_seo_audit_checklist():
    """Generate the SEO Audit Checklist PDF"""
    print("Creating: 100-Point SEO Audit Checklist...")
    
    filename = "resources/100-point-seo-audit-checklist.pdf"
    os.makedirs("resources", exist_ok=True)
    
    doc = SimpleDocTemplate(filename, pagesize=letter, topMargin=1*inch, bottomMargin=0.75*inch)
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=BLUE,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=DARK_GRAY,
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=PURPLE,
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    # Title page
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("🚀", title_style))
    story.append(Paragraph("100-Point SEO Audit Checklist", title_style))
    story.append(Paragraph("Complete Website Audit Guide for Indian Businesses", subtitle_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Use this comprehensive checklist to audit any website's SEO performance. Each section includes actionable items you can check off as you complete them.", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>How to Use This Checklist:</b>", styles['Normal']))
    story.append(Paragraph("• Go through each section systematically<br/>• Check off items as you complete them<br/>• Each item = 1 point (100 points total)<br/>• Score 80+ = Excellent, 60-79 = Good, Below 60 = Needs Work", styles['Normal']))
    
    story.append(PageBreak())
    
    # Section 1: On-Page SEO (25 points)
    story.append(Paragraph("1. On-Page SEO Checklist (25 Points)", heading_style))
    
    onpage_items = [
        ("☐", "<b>Title Tags Optimized:</b> Each page has unique, keyword-rich title (50-60 characters)"),
        ("☐", "<b>Meta Descriptions:</b> Compelling descriptions for all pages (150-160 characters)"),
        ("☐", "<b>H1 Tags:</b> One H1 per page with primary keyword included"),
        ("☐", "<b>H2-H6 Structure:</b> Logical heading hierarchy throughout content"),
        ("☐", "<b>URL Structure:</b> Clean, descriptive URLs with keywords (avoid numbers/symbols)"),
        ("☐", "<b>Keyword Placement:</b> Primary keyword in first 100 words of content"),
        ("☐", "<b>Keyword Density:</b> 1-2% keyword density (not stuffed)"),
        ("☐", "<b>LSI Keywords:</b> Related keywords naturally included in content"),
        ("☐", "<b>Content Length:</b> Minimum 1000 words for important pages"),
        ("☐", "<b>Content Quality:</b> Original, valuable content (not AI-generated spam)"),
        ("☐", "<b>Image Alt Text:</b> All images have descriptive alt text with keywords"),
        ("☐", "<b>Image File Names:</b> Descriptive file names (e.g., mumbai-seo-services.jpg)"),
        ("☐", "<b>Image Compression:</b> All images optimized (under 100KB when possible)"),
        ("☐", "<b>Internal Links:</b> 3-5 relevant internal links per page"),
        ("☐", "<b>External Links:</b> 2-3 authoritative external links per page"),
        ("☐", "<b>Anchor Text:</b> Descriptive anchor text (not 'click here')"),
        ("☐", "<b>Broken Links:</b> No 404 errors or broken internal/external links"),
        ("☐", "<b>Content Freshness:</b> Recently updated (within last 6 months)"),
        ("☐", "<b>Readability:</b> Easy to read (Flesch score 60+)"),
        ("☐", "<b>Mobile Formatting:</b> Content readable on mobile devices"),
        ("☐", "<b>CTA Buttons:</b> Clear call-to-action on every page"),
        ("☐", "<b>Contact Info:</b> Easy to find contact information"),
        ("☐", "<b>Social Sharing:</b> Social media share buttons present"),
        ("☐", "<b>Schema Markup:</b> Relevant schema for page type (Article, Product, etc.)"),
        ("☐", "<b>Content Updates:</b> Date stamps showing content freshness"),
    ]
    
    for checkbox, item in onpage_items:
        story.append(Paragraph(f"{checkbox} {item}", styles['Normal']))
        story.append(Spacer(1, 8))
    
    story.append(PageBreak())
    
    # Section 2: Technical SEO (25 points)
    story.append(Paragraph("2. Technical SEO Checklist (25 Points)", heading_style))
    
    technical_items = [
        ("☐", "<b>HTTPS Enabled:</b> SSL certificate installed (secure padlock in browser)"),
        ("☐", "<b>Mobile-Friendly:</b> Passes Google Mobile-Friendly Test"),
        ("☐", "<b>Page Speed:</b> Loads in under 3 seconds (test with PageSpeed Insights)"),
        ("☐", "<b>Core Web Vitals:</b> Green scores for LCP, FID, CLS"),
        ("☐", "<b>XML Sitemap:</b> Sitemap.xml exists and submitted to Google Search Console"),
        ("☐", "<b>Robots.txt:</b> Properly configured robots.txt file"),
        ("☐", "<b>Canonical Tags:</b> Canonical tags prevent duplicate content issues"),
        ("☐", "<b>404 Page:</b> Custom 404 page with helpful navigation"),
        ("☐", "<b>Site Architecture:</b> Max 3 clicks to reach any page"),
        ("☐", "<b>Breadcrumbs:</b> Breadcrumb navigation implemented"),
        ("☐", "<b>Pagination:</b> Properly implemented rel='next' and rel='prev' tags"),
        ("☐", "<b>Redirects:</b> 301 redirects for old URLs (no 302s)"),
        ("☐", "<b>No Redirect Chains:</b> URLs redirect only once"),
        ("☐", "<b>Image Lazy Loading:</b> Lazy loading enabled for images"),
        ("☐", "<b>Browser Caching:</b> Cache headers configured (check GTmetrix)"),
        ("☐", "<b>Gzip Compression:</b> Text files compressed with Gzip"),
        ("☐", "<b>CDN Usage:</b> Content Delivery Network for faster loading"),
        ("☐", "<b>Minified CSS/JS:</b> CSS and JavaScript files minified"),
        ("☐", "<b>Structured Data:</b> JSON-LD structured data validated"),
        ("☐", "<b>AMP Pages:</b> AMP version for blog posts (optional but helpful)"),
        ("☐", "<b>Hreflang Tags:</b> If multi-language, proper hreflang implementation"),
        ("☐", "<b>JavaScript SEO:</b> Content visible with JavaScript disabled"),
        ("☐", "<b>Server Response:</b> 200 status codes for all important pages"),
        ("☐", "<b>Log File Analysis:</b> Regular server log analysis for crawl errors"),
        ("☐", "<b>Uptime Monitoring:</b> Site monitored for downtime (99%+ uptime)"),
    ]
    
    for checkbox, item in technical_items:
        story.append(Paragraph(f"{checkbox} {item}", styles['Normal']))
        story.append(Spacer(1, 8))
    
    story.append(PageBreak())
    
    # Section 3: Off-Page SEO (25 points)
    story.append(Paragraph("3. Off-Page SEO Checklist (25 Points)", heading_style))
    
    offpage_items = [
        ("☐", "<b>Backlink Profile:</b> 10+ quality backlinks from relevant sites"),
        ("☐", "<b>Domain Authority:</b> Domain Authority 20+ (check Moz/Ahrefs)"),
        ("☐", "<b>No Toxic Links:</b> Disavowed any spammy or toxic backlinks"),
        ("☐", "<b>Link Diversity:</b> Links from various domains (not just one source)"),
        ("☐", "<b>Anchor Text Variety:</b> Mix of branded, exact match, and generic anchors"),
        ("☐", "<b>DoFollow Links:</b> Majority of links are DoFollow"),
        ("☐", "<b>Guest Posting:</b> Guest posts on 3+ relevant blogs"),
        ("☐", "<b>Directory Listings:</b> Listed in JustDial, Sulekha, IndiaMART"),
        ("☐", "<b>Social Profiles:</b> Active profiles on Facebook, LinkedIn, Twitter"),
        ("☐", "<b>Social Signals:</b> Regular social media posts with engagement"),
        ("☐", "<b>Google My Business:</b> Verified and optimized GMB profile"),
        ("☐", "<b>NAP Consistency:</b> Same Name/Address/Phone across all platforms"),
        ("☐", "<b>Local Citations:</b> Listed in 10+ local directories"),
        ("☐", "<b>Customer Reviews:</b> 10+ positive Google reviews"),
        ("☐", "<b>Review Responses:</b> Responded to all reviews (positive and negative)"),
        ("☐", "<b>Brand Mentions:</b> Unlinked brand mentions (monitor with Google Alerts)"),
        ("☐", "<b>Competitor Backlinks:</b> Analyzed and targeted competitor backlink sources"),
        ("☐", "<b>Resource Pages:</b> Links from resource/tools pages"),
        ("☐", "<b>Industry Forums:</b> Active participation in relevant forums"),
        ("☐", "<b>Q&A Sites:</b> Helpful answers on Quora, Reddit with links"),
        ("☐", "<b>Press Releases:</b> At least one press release distributed"),
        ("☐", "<b>Influencer Outreach:</b> Collaborated with micro-influencers"),
        ("☐", "<b>Podcast/Video:</b> Featured on podcasts or YouTube videos"),
        ("☐", "<b>Testimonials:</b> Given testimonials to tools/services you use"),
        ("☐", "<b>Link Building Strategy:</b> Documented ongoing link building plan"),
    ]
    
    for checkbox, item in offpage_items:
        story.append(Paragraph(f"{checkbox} {item}", styles['Normal']))
        story.append(Spacer(1, 8))
    
    story.append(PageBreak())
    
    # Section 4: Local SEO (25 points)
    story.append(Paragraph("4. Local SEO Checklist (25 Points)", heading_style))
    
    local_items = [
        ("☐", "<b>GMB Claimed:</b> Google My Business profile claimed and verified"),
        ("☐", "<b>GMB Complete:</b> 100% profile completion (all fields filled)"),
        ("☐", "<b>GMB Category:</b> Correct primary and additional categories selected"),
        ("☐", "<b>GMB Description:</b> Keyword-rich 750-character description"),
        ("☐", "<b>Business Hours:</b> Accurate hours, updated for holidays"),
        ("☐", "<b>GMB Photos:</b> 20+ high-quality photos uploaded"),
        ("☐", "<b>Cover Photo:</b> Professional cover photo showcasing business"),
        ("☐", "<b>Logo:</b> High-resolution logo uploaded"),
        ("☐", "<b>Services Listed:</b> All services/products listed in GMB"),
        ("☐", "<b>Attributes:</b> All relevant attributes selected"),
        ("☐", "<b>Q&A Section:</b> 5+ questions answered in Q&A"),
        ("☐", "<b>Google Posts:</b> Weekly Google Posts about offers/updates"),
        ("☐", "<b>Booking Button:</b> Booking/appointment button enabled"),
        ("☐", "<b>Local Keywords:</b> City/area names in title tags and content"),
        ("☐", "<b>Location Pages:</b> Separate pages for each service area"),
        ("☐", "<b>Local Schema:</b> LocalBusiness schema markup implemented"),
        ("☐", "<b>NAP on Website:</b> Name, Address, Phone in footer of every page"),
        ("☐", "<b>Google Maps Embed:</b> Google Maps embedded on contact page"),
        ("☐", "<b>Service Area:</b> Service area clearly defined on website"),
        ("☐", "<b>Local Content:</b> Blog posts about local events/news"),
        ("☐", "<b>Bing Places:</b> Claimed and optimized Bing Places listing"),
        ("☐", "<b>Apple Maps:</b> Business listed on Apple Maps"),
        ("☐", "<b>Local Backlinks:</b> Links from local news sites/blogs"),
        ("☐", "<b>Chamber of Commerce:</b> Listed in local chamber directory"),
        ("☐", "<b>Local Sponsorships:</b> Sponsor local events for backlinks/visibility"),
    ]
    
    for checkbox, item in local_items:
        story.append(Paragraph(f"{checkbox} {item}", styles['Normal']))
        story.append(Spacer(1, 8))
    
    story.append(PageBreak())
    
    # Scoring section
    story.append(Paragraph("📊 How to Calculate Your Score", heading_style))
    story.append(Spacer(1, 12))
    
    scoring_data = [
        ['Score Range', 'Grade', 'Action Needed'],
        ['90-100 points', 'Excellent', 'Maintain and monitor'],
        ['80-89 points', 'Very Good', 'Minor improvements'],
        ['70-79 points', 'Good', 'Focus on weak areas'],
        ['60-69 points', 'Fair', 'Significant improvements needed'],
        ['Below 60', 'Needs Work', 'Major SEO overhaul required'],
    ]
    
    scoring_table = Table(scoring_data, colWidths=[1.5*inch, 1.5*inch, 3*inch])
    scoring_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), 'lightgrey'),
        ('GRID', (0, 0), (-1, -1), 1, 'black'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), ['white', HexColor('#F3F4F6')]),
    ]))
    
    story.append(scoring_table)
    story.append(Spacer(1, 24))
    
    story.append(Paragraph("<b>Next Steps:</b>", styles['Normal']))
    story.append(Paragraph("1. Work through each section systematically<br/>2. Focus on high-impact items first (Technical SEO is foundation)<br/>3. Re-audit every 3 months to maintain SEO health<br/>4. Need help? Check out our affordable coaching at TractionSEO", styles['Normal']))
    
    # Build PDF
    doc.build(story, onFirstPage=create_header_footer, onLaterPages=create_header_footer)
    print(f"✅ Created: {filename}")
    return filename

# ============================================================================
# PDF 2: 50+ ChatGPT Prompts for SEO
# ============================================================================

def create_chatgpt_prompts():
    """Generate the ChatGPT Prompts PDF"""
    print("Creating: 50+ ChatGPT Prompts for SEO...")
    
    filename = "resources/50-chatgpt-prompts-for-seo.pdf"
    
    doc = SimpleDocTemplate(filename, pagesize=letter, topMargin=1*inch, bottomMargin=0.75*inch)
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles (same as above)
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=BLUE,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=DARK_GRAY,
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=PURPLE,
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    prompt_style = ParagraphStyle(
        'PromptStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=DARK_GRAY,
        leftIndent=20,
        rightIndent=20,
        spaceBefore=8,
        spaceAfter=8,
        backColor=HexColor('#F3F4F6'),
        borderPadding=10,
        borderRadius=5
    )
    
    # Title page
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("✨", title_style))
    story.append(Paragraph("50+ ChatGPT Prompts for SEO Success", title_style))
    story.append(Paragraph("Copy-Paste Ready Prompts for Indian Businesses", subtitle_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("This collection contains 50+ proven ChatGPT prompts for every aspect of SEO. Simply copy, paste into ChatGPT, customize the bracketed sections [like this], and get instant results.", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>How to Use:</b> Replace [bracketed text] with your specific information. For best results, provide context about your business, industry, and target audience.", styles['Normal']))
    
    story.append(PageBreak())
    
    # Section 1: Keyword Research Prompts
    story.append(Paragraph("1. Keyword Research Prompts (10)", heading_style))
    
    keyword_prompts = [
        ("Keyword Ideation", "Generate 50 long-tail keyword ideas for [your niche/industry] targeting [Indian city/region]. Include search intent (informational, commercial, transactional) and estimated difficulty level for each keyword."),
        ("Competitor Keywords", "Analyze the top 5 competitors for [your primary keyword]. What keywords are they ranking for that I'm not? Suggest 20 keyword opportunities where I can outrank them."),
        ("Local Keywords", "Generate 30 local SEO keywords for a [business type] in [Indian city]. Include 'near me' variations, neighborhood names, and local landmarks."),
        ("Question Keywords", "List 25 question-based keywords (what, how, why, when, where) related to [your topic]. These will be perfect for blog posts and FAQ sections."),
        ("LSI Keywords", "Provide 20 LSI (Latent Semantic Indexing) keywords related to [your primary keyword]. These help Google understand content context better."),
        ("Seasonal Keywords", "Suggest 15 seasonal keywords for [your business] in India. Include festivals, exam seasons, wedding seasons, and other timing-based opportunities."),
        ("Keyword Clustering", "Take these keywords [list 10-20 keywords] and group them into topical clusters. Suggest pillar pages and supporting content for each cluster."),
        ("Voice Search Keywords", "Generate 20 voice search keywords for [your business/topic]. Focus on conversational, natural language queries that Indians actually speak."),
        ("Regional Language Keywords", "Suggest keyword variations in Hinglish (Hindi + English mix) for [your topic]. Many Indians search in mixed language - this is a goldmine opportunity."),
        ("Keyword Gap Analysis", "I rank for these keywords: [list yours]. My competitor ranks for: [list theirs]. What's the gap? Which keywords should I prioritize to close this gap?"),
    ]
    
    for i, (title, prompt) in enumerate(keyword_prompts, 1):
        story.append(Paragraph(f"<b>Prompt {i}: {title}</b>", styles['Normal']))
        story.append(Paragraph(f'"{prompt}"', prompt_style))
        story.append(Spacer(1, 12))
    
    story.append(PageBreak())
    
    # Section 2: Content Creation Prompts
    story.append(Paragraph("2. Content Creation Prompts (15)", heading_style))
    
    content_prompts = [
        ("Blog Outline", "Create a detailed blog post outline for '[your keyword]' targeting Indian readers. Include: Introduction hook, 5-7 H2 sections with 3-4 H3 subsections each, key points to cover, and a compelling conclusion with CTA."),
        ("Meta Title Generator", "Generate 10 SEO-optimized meta titles for a page about [your topic]. Each should be 50-60 characters, include the primary keyword, and be compelling enough to get clicks."),
        ("Meta Description Writer", "Write 5 meta descriptions for [your page/topic]. Each should be 150-160 characters, include a call-to-action, and mention benefits for Indian businesses/users."),
        ("Introduction Paragraph", "Write an engaging introduction paragraph for an article about [your topic]. Hook the reader in the first sentence, mention the pain point, and promise a solution. Target Indian audience."),
        ("FAQ Generator", "Generate 10 frequently asked questions and detailed answers about [your topic/service]. Format them for FAQ schema markup."),
        ("Product Description", "Write a compelling 150-word product description for [your product]. Include key features, benefits, and target keywords naturally. Focus on Indian market needs."),
        ("Service Page Content", "Create comprehensive content for a service page about [your service]. Include: What it is, how it works, benefits, pricing for Indian market, FAQs, and trust signals."),
        ("Case Study Outline", "Create an outline for a case study showing how [your solution] helped [client type]. Include: Challenge, Solution, Implementation, Results with metrics, Testimonial, and Key Takeaways."),
        ("Social Media Captions", "Write 5 engaging social media captions for posts about [your topic]. Include relevant hashtags for Indian audience, a hook, value proposition, and CTA. Keep under 100 words."),
        ("Email Newsletter", "Write a 200-word newsletter introducing [your new content/product/service] to subscribers. Make it conversational, benefit-focused, and include a clear call-to-action."),
        ("How-To Guide Structure", "Create a step-by-step how-to guide structure for '[how to do X]'. Break it into 7-10 clear steps with descriptions. Include what tools/materials are needed."),
        ("Comparison Article", "Create an outline for '[Option A] vs [Option B]: Which is Better for Indian Businesses?' Include: Introduction, Feature comparison table, Pros/Cons, Use cases, Pricing in INR, and Verdict."),
        ("Listicle Structure", "Create an outline for 'Top 10 [Topic] for [Indian audience]'. Include catchy title, introduction, each item with description and why it's valuable, and conclusion."),
        ("Content Refresh", "I have this old content: [paste excerpt]. Help me refresh it for 2025. Update statistics, add new trends, improve readability, and suggest 3-5 new sections to add."),
        ("Regional Language Content", "Translate this content to Hinglish (keep it natural, not literal translation): [your English content]. Ensure it sounds conversational and culturally appropriate for Indian readers."),
    ]
    
    for i, (title, prompt) in enumerate(content_prompts, 11):
        story.append(Paragraph(f"<b>Prompt {i}: {title}</b>", styles['Normal']))
        story.append(Paragraph(f'"{prompt}"', prompt_style))
        story.append(Spacer(1, 12))
        if i == 17:  # Page break mid-section
            story.append(PageBreak())
    
    story.append(PageBreak())
    
    # Section 3: Technical SEO Prompts
    story.append(Paragraph("3. Technical SEO Prompts (10)", heading_style))
    
    technical_prompts = [
        ("Schema Markup Generator", "Generate JSON-LD schema markup for [Article/LocalBusiness/Product/FAQ] with these details: [provide your details]. Ensure it's valid and includes all required fields."),
        ("Robots.txt Creator", "Create a robots.txt file for my [type of website]. I want to allow all search engines, block admin pages at /admin/, and reference my sitemap at domain.com/sitemap.xml."),
        ("Canonical Tag Strategy", "I have these URLs that show the same content: [list URLs]. How should I implement canonical tags? Which URL should be canonical and what tags should the others have?"),
        ("Hreflang Tags", "I have these language versions: English (en-in), Hindi (hi-in), Tamil (ta-in). Generate proper hreflang tags for a page at [URL] with versions at [Hindi URL] and [Tamil URL]."),
        ("Site Speed Optimization", "My PageSpeed Insights shows: LCP 4.2s, FID 200ms, CLS 0.25. Provide a prioritized action plan to improve these scores. Focus on quick wins first."),
        ("Mobile Optimization", "My site fails Google Mobile-Friendly Test with these issues: [paste errors]. Provide specific fixes and code examples to resolve each issue."),
        ("301 Redirect Rules", "I'm changing my URL structure from [old format] to [new format]. Generate .htaccess 301 redirect rules for these 10 old URLs: [list URLs] to their new versions."),
        ("XML Sitemap Structure", "I have a [type of site] with [number] pages, [number] blog posts, and [number] products. Suggest an optimal XML sitemap structure. Should I use index sitemaps?"),
        ("Structured Data for FAQ", "Convert these 5 FAQs into proper FAQ schema markup: [list your Q&As]. Provide complete JSON-LD code ready to paste in my HTML."),
        ("Core Web Vitals Fix", "My Core Web Vitals failed with: [specific issues from PageSpeed Insights]. Provide a step-by-step technical action plan with code examples to fix each issue."),
    ]
    
    for i, (title, prompt) in enumerate(technical_prompts, 26):
        story.append(Paragraph(f"<b>Prompt {i}: {title}</b>", styles['Normal']))
        story.append(Paragraph(f'"{prompt}"', prompt_style))
        story.append(Spacer(1, 12))
    
    story.append(PageBreak())
    
    # Section 4: Competitor Analysis Prompts
    story.append(Paragraph("4. Competitor Analysis Prompts (8)", heading_style))
    
    competitor_prompts = [
        ("Competitor Content Gap", "My competitor [domain] ranks for these topics: [list 5-10 topics]. I cover: [your topics]. What content gaps should I fill to compete effectively in the Indian market?"),
        ("Backlink Analysis", "Analyze my competitor's backlink profile at [domain]. What types of sites link to them? Suggest 10 sites I should target for backlinks in the Indian market."),
        ("Content Length Analysis", "My top 5 competitors for [keyword] have content of these lengths: [list word counts]. What's the ideal length for my content to outrank them? What unique angles can I add?"),
        ("Keyword Overlap", "I rank for [list your top 10 keywords]. My competitor ranks for [their top 10]. Where do we overlap? Where do they beat me? Suggest a strategy to outrank them on overlap keywords."),
        ("SERP Feature Analysis", "For keyword [X], the SERP has: Featured snippet, People Also Ask, Local Pack, Videos. Which of these can I target? Provide a strategy for each SERP feature."),
        ("Competitor's Best Content", "Analyze [competitor domain]'s most linked-to and shared content. What makes it successful? Suggest 3 content ideas I can create to compete, with an Indian audience angle."),
        ("Social Media Strategy", "My competitor has [X] followers on [platform] with this posting frequency: [describe]. Analyze their strategy. What's working? How can I differentiate while reaching Indian audience?"),
        ("Pricing Comparison", "My competitors charge: [list competitor pricing in INR]. My service offers [your unique value]. How should I position my pricing for the Indian market to be competitive yet profitable?"),
    ]
    
    for i, (title, prompt) in enumerate(competitor_prompts, 36):
        story.append(Paragraph(f"<b>Prompt {i}: {title}</b>", styles['Normal']))
        story.append(Paragraph(f'"{prompt}"', prompt_style))
        story.append(Spacer(1, 12))
    
    story.append(PageBreak())
    
    # Section 5: Link Building Prompts
    story.append(Paragraph("5. Link Building Prompts (8)", heading_style))
    
    link_prompts = [
        ("Outreach Email Template", "Write a personalized outreach email to [website owner] requesting a backlink to my article about [your topic]. Make it benefit-focused, not salesy. Keep under 150 words."),
        ("Guest Post Pitch", "Create a guest post pitch for [website/blog name] in the [Indian/niche] space. Suggest 3 article ideas relevant to their audience, explain my expertise, and keep it professional yet friendly."),
        ("Resource Page Link Request", "Write an email requesting to be added to this resource page: [URL of resource page]. Explain why my [resource/tool/guide] would be valuable to their audience. Keep it brief."),
        ("Broken Link Building", "I found this broken link on [website]: [broken URL]. My resource at [your URL] is a perfect replacement. Write an outreach email informing them and suggesting my link."),
        ("Testimonial for Backlink", "Write a genuine testimonial for [tool/service name] that I use. Include specific benefits and results I've achieved. This testimonial will earn me a backlink from their site."),
        ("HARO Response", "A journalist asked: '[HARO query]'. Write a 100-word expert response that provides value, establishes my credibility, and includes my business name and website subtly."),
        ("Infographic Outreach", "I created an infographic about [topic] at [URL]. Write an outreach email to [website] suggesting they embed it in their article about [related topic]. Include embed code."),
        ("Link Reclamation", "My brand [Brand Name] was mentioned on [website] at [URL] without a link. Write a friendly email asking them to add a link to my site at [your URL]. Keep it short and appreciative."),
    ]
    
    for i, (title, prompt) in enumerate(link_prompts, 44):
        story.append(Paragraph(f"<b>Prompt {i}: {title}</b>", styles['Normal']))
        story.append(Paragraph(f'"{prompt}"', prompt_style))
        story.append(Spacer(1, 12))
    
    story.append(PageBreak())
    
    # Bonus Section
    story.append(Paragraph("💎 Bonus: Advanced SEO Prompts (4)", heading_style))
    
    bonus_prompts = [
        ("SEO Strategy Plan", "Create a complete 6-month SEO strategy for [type of business] in [Indian city]. Include: Keyword targets, content calendar, link building plan, technical improvements, and expected ROI. Budget: [amount]."),
        ("Content Cluster Strategy", "I want to rank for '[main topic]'. Create a pillar page + cluster content strategy. Suggest 1 pillar page and 8-10 cluster articles, with keyword targets for each."),
        ("Local SEO Audit", "Audit my local SEO for [business name] in [city]. Check: GMB optimization, NAP consistency, local citations, reviews, local content. Provide a prioritized fix list."),
        ("AI Content Detection Fix", "My content is being flagged as AI-generated. Help me humanize it. Here's a paragraph: [paste]. Rewrite it to sound more natural, add personal examples, and include conversational elements."),
    ]
    
    for i, (title, prompt) in enumerate(bonus_prompts, 52):
        story.append(Paragraph(f"<b>Prompt {i}: {title}</b>", styles['Normal']))
        story.append(Paragraph(f'"{prompt}"', prompt_style))
        story.append(Spacer(1, 12))
    
    story.append(Spacer(1, 24))
    story.append(Paragraph("🎯 <b>Pro Tips for Better Results:</b>", styles['Normal']))
    story.append(Paragraph("• Be specific - Replace ALL bracketed [text] with your actual details<br/>• Provide context - Tell ChatGPT about your business, audience, and goals<br/>• Iterate - If the first response isn't perfect, ask ChatGPT to refine it<br/>• Combine prompts - Mix and match these prompts for complex tasks<br/>• Stay updated - Save successful prompts and keep testing new variations", styles['Normal']))
    
    # Build PDF
    doc.build(story, onFirstPage=create_header_footer, onLaterPages=create_header_footer)
    print(f"✅ Created: {filename}")
    return filename

# ============================================================================
# PDF 3: Local SEO Blueprint for Indian Businesses
# ============================================================================

def create_local_seo_blueprint():
    """Generate the Local SEO Blueprint PDF"""
    print("Creating: Local SEO Blueprint for Indian Businesses...")
    
    filename = "resources/local-seo-blueprint-india.pdf"
    
    doc = SimpleDocTemplate(filename, pagesize=letter, topMargin=1*inch, bottomMargin=0.75*inch)
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=BLUE,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=DARK_GRAY,
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=PURPLE,
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubheading',
        parent=styles['Heading3'],
        fontSize=13,
        textColor=ORANGE,
        spaceAfter=8,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    prompt_style = ParagraphStyle(
        'PromptBox',
        parent=styles['Normal'],
        fontSize=10,
        textColor=DARK_GRAY,
        backColor=HexColor('#F3F4F6'),
        borderColor=LIGHT_GRAY,
        borderWidth=1,
        borderPadding=8,
        spaceAfter=12,
        leftIndent=12,
        rightIndent=12
    )
    
    # Title page
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("📍", title_style))
    story.append(Paragraph("Local SEO Blueprint for Indian Businesses", title_style))
    story.append(Paragraph("Complete Guide to Dominating 'Near Me' Searches in India", subtitle_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Local SEO is the most powerful marketing channel for Indian small businesses. This blueprint provides everything you need to dominate local search results, get more customers from Google, and outrank your competitors.", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>What's Inside:</b> Google Business Profile optimization, 100+ Indian citation sources, review generation strategies, local content templates, and real success stories from Indian businesses.", styles['Normal']))
    
    story.append(PageBreak())
    
    # Chapter 1: Google Business Profile Optimization
    story.append(Paragraph("Chapter 1: Google Business Profile Mastery", heading_style))
    story.append(Paragraph("Your Google Business Profile (GBP) is the foundation of local SEO. A well-optimized GBP can generate 200-500 leads per month completely free.", styles['Normal']))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("1.1 Claiming and Verifying Your Profile", subheading_style))
    story.append(Paragraph("<b>Step 1:</b> Go to google.com/business<br/><b>Step 2:</b> Search for your business name<br/><b>Step 3:</b> If found, claim it. If not, create new listing<br/><b>Step 4:</b> Verify via postcard (takes 5-7 days in India)<br/><b>Step 5:</b> Once verified, log in to edit", styles['Normal']))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("1.2 100% Profile Completion Checklist", subheading_style))
    story.append(Paragraph("Google rewards complete profiles with better rankings. Fill EVERY field:", styles['Normal']))
    
    gmb_checklist = [
        "☐ Business Name (exact legal name, no keywords)",
        "☐ Primary Category (most important - choose carefully)",
        "☐ Additional Categories (up to 9 more)",
        "☐ Business Address (exact, with proper pin code)",
        "☐ Service Area (list all areas you serve, max 20)",
        "☐ Phone Number (local Indian number, not toll-free)",
        "☐ Website URL (link to your main website)",
        "☐ Business Hours (accurate, update for holidays)",
        "☐ Business Description (750 chars, keyword-rich)",
        "☐ Opening Date (when you started)",
        "☐ Attributes (all relevant ones: Wi-Fi, parking, etc.)",
    ]
    
    for item in gmb_checklist:
        story.append(Paragraph(item, styles['Normal']))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("1.3 Photo Requirements (Critical!)", subheading_style))
    story.append(Paragraph("Businesses with photos get 42% more direction requests and 35% more website clicks. Upload:", styles['Normal']))
    
    photo_guide = [
        "• Logo: Square format, min 720x720px, high resolution",
        "• Cover Photo: Landscape, showcases your best offering",
        "• Interior Photos: 10-15 photos showing ambiance, seating",
        "• Exterior Photos: Storefront, parking, nearby landmarks",
        "• Product/Service Photos: 20-30 photos of what you sell",
        "• Team Photos: Staff in action (builds trust)",
        "• Menu/Price List: If applicable, very important for restaurants",
    ]
    
    for item in photo_guide:
        story.append(Paragraph(item, styles['Normal']))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("1.4 Perfect Business Description Template", subheading_style))
    story.append(Paragraph("Here's a template for your 750-character description:", styles['Normal']))
    
    description_template = """
    "[Business Name] - [Type of business] in [Area] since [Year]. We offer [main services/products] 
    to customers across [service areas]. Known for [unique selling point], we've served [number]+ 
    happy customers. Open daily [hours]. Services include: [service 1], [service 2], [service 3]. 
    We specialize in [specialty]. [Unique benefit: e.g., "Same-day delivery in Mumbai"]. Popular for: 
    [popular item 1], [popular item 2]. [Award/certification if any]. Call [phone] or visit 
    [address] for [action: quote/consultation/service]."
    """
    
    story.append(Paragraph(description_template, prompt_style))
    
    story.append(PageBreak())
    
    # Chapter 2: Review Generation & Management
    story.append(Paragraph("Chapter 2: Reviews - Your Ranking Powerhouse", heading_style))
    story.append(Paragraph("Reviews are the #1 ranking factor for local SEO. Here's how to get them ethically and respond effectively.", styles['Normal']))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("2.1 How to Get More Reviews (The Right Way)", subheading_style))
    
    review_strategies = [
        ("<b>Create Your Review Link:</b>", "Go to GBP → Share → Copy Short URL (g.page/yourbusiness/review)"),
        ("<b>Ask In Person:</b>", "After great service: 'Would you mind leaving us a quick Google review?'"),
        ("<b>WhatsApp/SMS:</b>", "Send review link 2-3 hours after purchase with thank you message"),
        ("<b>Print Materials:</b>", "QR code on bills, receipts, business cards, table tents"),
        ("<b>Email Follow-Up:</b>", "Automated email 2-3 days after purchase with review link"),
        ("<b>Social Media:</b>", "Post your review link on Instagram/Facebook stories monthly"),
        ("<b>Incentivize Ethically:</b>", "Small gift for ALL customers, not just reviewers (stays within guidelines)"),
    ]
    
    for title, desc in review_strategies:
        story.append(Paragraph(f"{title} {desc}", styles['Normal']))
        story.append(Spacer(1, 6))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("⚠️ <b>NEVER Do These (Google Will Penalize):</b>", styles['Normal']))
    never_do = [
        "❌ Buy fake reviews from Fiverr/freelance sites",
        "❌ Offer discounts specifically for reviews",
        "❌ Write reviews from your own devices/network",
        "❌ Have employees leave reviews",
        "❌ Create fake customer accounts",
    ]
    
    for item in never_do:
        story.append(Paragraph(item, styles['Normal']))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("2.2 Response Templates (Copy-Paste Ready)", subheading_style))
    story.append(Paragraph("<b>For 5-Star Reviews:</b>", styles['Normal']))
    story.append(Paragraph('"Thank you so much, [Name]! We\'re thrilled you loved our [specific thing they mentioned]. We look forward to serving you again soon! 🙏 - [Your Name], [Business Name]"', prompt_style))
    
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>For 3-Star Reviews:</b>", styles['Normal']))
    story.append(Paragraph('"Hi [Name], thank you for your feedback. We appreciate you mentioning [positive thing]. Regarding [issue], we\'d love to make it right. Please call us at [phone] or email [email]. - [Your Name]"', prompt_style))
    
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>For 1-Star Reviews:</b>", styles['Normal']))
    story.append(Paragraph('"We\'re sorry to hear about your experience, [Name]. This isn\'t the standard we set for ourselves. We\'ve sent you a direct message to resolve this. We value your feedback and want to make this right. - [Your Name]"', prompt_style))
    
    story.append(PageBreak())
    
    # Chapter 3: Indian Citation Sources
    story.append(Paragraph("Chapter 3: 100+ Indian Citation Sources", heading_style))
    story.append(Paragraph("Citations are online mentions of your business Name, Address, and Phone (NAP). They significantly boost local rankings. Here are the top Indian directories:", styles['Normal']))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("3.1 Essential Indian Directories (Do These First)", subheading_style))
    
    essential_citations = [
        ("JustDial", "justdial.com - #1 Indian directory, mandatory for every business"),
        ("Sulekha", "sulekha.com - High authority, strong local presence"),
        ("IndiaMART", "indiamart.com - Critical for B2B businesses"),
        ("Facebook Business", "facebook.com/business - Create complete business page"),
        ("Bing Places", "bingplaces.com - Often forgotten, easy win"),
        ("Apple Maps", "mapsconnect.apple.com - Growing in India, claim your listing"),
        ("Yelp India", "yelp.in - Especially for restaurants and services"),
        ("Zomato", "zomato.com - Mandatory for restaurants"),
        ("Swiggy", "swiggy.com - Food delivery + visibility"),
        ("UrbanClap", "urbancompany.com - Service businesses"),
    ]
    
    for name, desc in essential_citations:
        story.append(Paragraph(f"<b>{name}:</b> {desc}", styles['Normal']))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("3.2 City-Specific Directories", subheading_style))
    
    city_directories = [
        ("<b>Mumbai:</b>", "AskLaila, Mumbai Live, BurppleMumbai, TimeOutMumbai"),
        ("<b>Delhi NCR:</b>", "DelhiInfo, NCRDays, SoDelhi, DforDelhi"),
        ("<b>Bangalore:</b>", "BangaloreBest, Insider Bangalore, BurppleBangalore"),
        ("<b>Hyderabad:</b>", "HyderabadPlanet, HYLife, Burrp Hyderabad"),
        ("<b>Chennai:</b>", "ChennaiOnline, ChennaiVista, EventsHigh Chennai"),
        ("<b>Pune:</b>", "Pune365, LocalWire Pune, YellowPages Pune"),
    ]
    
    for city, dirs in city_directories:
        story.append(Paragraph(f"{city} {dirs}", styles['Normal']))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("3.3 Industry-Specific Directories (Choose Relevant Ones)", subheading_style))
    
    industry_dirs = [
        "• <b>Restaurants:</b> Zomato, Swiggy, EazyDiner, Dineout, Magicpin, Tripadvisor",
        "• <b>Healthcare:</b> Practo, Lybrate, 1mg, DocPrime, JustDoc",
        "• <b>Education:</b> Shiksha, CollegeDunia, Careers360, MBAUniverse",
        "• <b>Real Estate:</b> 99acres, MagicBricks, Housing.com, CommonFloor",
        "• <b>Automotive:</b> CarDekho, BikeWale, Zigwheels, CarTrade",
        "• <b>Beauty/Salon:</b> UrbanClap, Stylpick, BeBeautiful, Nykaa",
        "• <b>Legal Services:</b> LawRato, Lawyered, Vakilsearch, MyAdvo",
        "• <b>Home Services:</b> UrbanClap, Housejoy, Zimmber, QuikrServices",
    ]
    
    for item in industry_dirs:
        story.append(Paragraph(item, styles['Normal']))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("3.4 NAP Consistency Rule (Critical!)", subheading_style))
    story.append(Paragraph("<b>Use EXACT same business information everywhere:</b>", styles['Normal']))
    story.append(Spacer(1, 8))
    
    nap_example = """
    ✅ Correct: "Raj's Biryani House, 123 Linking Road, Bandra West, Mumbai 400050, +91-9876543210"
    
    ❌ Wrong variations that hurt SEO:
    - "Raj Biryani House" (missing apostrophe)
    - "Linking Rd" (abbreviated)
    - "Bandra, Mumbai" (missing West)
    - "400-050" (dash in pin code)
    - "98765 43210" (space in phone)
    
    Even small differences confuse Google and hurt rankings!
    """
    
    story.append(Paragraph(nap_example, prompt_style))
    
    story.append(PageBreak())
    
    # Chapter 4: Local Content Strategy
    story.append(Paragraph("Chapter 4: Local Content That Ranks", heading_style))
    story.append(Paragraph("Creating location-specific content helps you rank for '[service] in [city]' searches. Here's your content playbook:", styles['Normal']))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("4.1 Location Pages Structure", subheading_style))
    story.append(Paragraph("Create dedicated pages for each area you serve:", styles['Normal']))
    
    location_page_structure = """
    <b>URL:</b> yoursite.com/[service]-[area-name]
    
    <b>Title Tag:</b> [Service] in [Area Name] | [Business Name]
    
    <b>H1:</b> [Service] in [Area Name]
    
    <b>Content Structure:</b>
    1. Introduction (mention area name, service)
    2. Why Choose Us in [Area]
    3. Our [Service] Process
    4. Service Areas We Cover (list nearby neighborhoods)
    5. Customer Reviews from [Area]
    6. Pricing for [Area] (if applicable)
    7. How to Reach Us (map, directions)
    8. FAQ about [Service] in [Area]
    
    <b>Pro Tip:</b> Mention local landmarks, neighborhoods, and pain points specific to that area.
    """
    
    story.append(Paragraph(location_page_structure, prompt_style))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("4.2 Local Blog Content Ideas (10 Topics)", subheading_style))
    
    blog_ideas = [
        "1. 'Top 10 [Your Service] Providers in [City] (Include yourself at #1)'",
        "2. '[Service] Cost in [City]: Complete Pricing Guide for 2025'",
        "3. 'Best Neighborhoods in [City] for [Your Niche]'",
        "4. 'How to Choose a [Your Business Type] in [City]: Complete Guide'",
        "5. '[City] [Your Industry] Guide: Everything You Need to Know'",
        "6. '[Number] Reasons Why [City] Residents Choose [Your Business]'",
        "7. '[Seasonal Topic] in [City]: Tips from Local Experts'",
        "8. 'Case Study: How We Helped a [City] Customer with [Problem]'",
        "9. '[City] Events Calendar: What's Happening This Month'",
        "10. 'Local Partnerships: Supporting [City] Businesses'",
    ]
    
    for idea in blog_ideas:
        story.append(Paragraph(idea, styles['Normal']))
    
    story.append(PageBreak())
    
    # Chapter 5: Success Stories
    story.append(Paragraph("Chapter 5: Real Success Stories from India", heading_style))
    story.append(Paragraph("Here are real examples of Indian businesses that dominated local SEO:", styles['Normal']))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("🏆 Case Study 1: Delhi Restaurant", subheading_style))
    story.append(Paragraph("<b>Business:</b> Small North Indian restaurant in Karol Bagh", styles['Normal']))
    story.append(Paragraph("<b>Starting Point:</b> 12 Google reviews, 500 monthly GMB views", styles['Normal']))
    story.append(Paragraph("<b>Actions Taken:</b><br/>• Optimized GBP 100%<br/>• Got 75 reviews in 3 months<br/>• Posted 3 photos weekly<br/>• Listed in 15 Indian directories", styles['Normal']))
    story.append(Paragraph("<b>Results (4 months):</b><br/>• GMB views: 500 → 8,500<br/>• Phone calls: 50 → 280/month<br/>• Direction requests: 800 → 3,200<br/>• Revenue: +180%", styles['Normal']))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("🏆 Case Study 2: Bangalore Salon", subheading_style))
    story.append(Paragraph("<b>Business:</b> Women's salon in Koramangala", styles['Normal']))
    story.append(Paragraph("<b>Starting Point:</b> Verified GMB, 20 reviews, minimal optimization", styles['Normal']))
    story.append(Paragraph("<b>Actions Taken:</b><br/>• Posted before/after photos daily<br/>• Used Google Posts for offers (2x/week)<br/>• Collected 120 reviews with photos<br/>• Created service-specific pages", styles['Normal']))
    story.append(Paragraph("<b>Results (5 months):</b><br/>• Bookings: 45 → 180/month<br/>• 85% customers from Google<br/>• 4.8-star rating (150+ reviews)<br/>• Revenue: ₹2.8L → ₹8.5L monthly", styles['Normal']))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("🏆 Case Study 3: Mumbai Plumber", subheading_style))
    story.append(Paragraph("<b>Business:</b> Plumbing services in Western suburbs", styles['Normal']))
    story.append(Paragraph("<b>Starting Point:</b> No online presence, word-of-mouth only", styles['Normal']))
    story.append(Paragraph("<b>Actions Taken:</b><br/>• Created & optimized GBP from scratch<br/>• Added service area (15 neighborhoods)<br/>• Got 40 reviews in 2 months<br/>• Created FAQ content for common issues", styles['Normal']))
    story.append(Paragraph("<b>Results (3 months):</b><br/>• Leads: 0 → 150+ monthly from Google<br/>• 75% conversion rate<br/>• Expanded team from 2 to 6 people<br/>• Now the #1 ranked plumber in Bandra", styles['Normal']))
    
    story.append(PageBreak())
    
    # Final Chapter: Action Plan
    story.append(Paragraph("Chapter 6: Your 60-Day Action Plan", heading_style))
    story.append(Paragraph("Follow this step-by-step plan to dominate local SEO in your area:", styles['Normal']))
    story.append(Spacer(1, 12))
    
    action_plan = [
        ("<b>Week 1-2: Foundation</b>", [
            "• Claim and verify Google Business Profile",
            "• Complete 100% of GBP fields",
            "• Upload 20+ high-quality photos",
            "• Create review link (g.page shortlink)",
            "• Print QR codes for review requests"
        ]),
        ("<b>Week 3-4: Citations</b>", [
            "• List on JustDial, Sulekha, IndiaMART",
            "• Create complete Facebook Business page",
            "• Claim Bing Places, Apple Maps",
            "• List on 5 industry-specific directories",
            "• Ensure NAP consistency everywhere"
        ]),
        ("<b>Week 5-6: Reviews</b>", [
            "• Ask every customer for reviews (Goal: 2-3/week)",
            "• Send WhatsApp follow-ups with review link",
            "• Respond to ALL existing reviews within 24 hours",
            "• Create email automation for review requests",
            "• Train staff to ask for reviews naturally"
        ]),
        ("<b>Week 7-8: Content & Optimization</b>", [
            "• Create 3 location-specific pages",
            "• Write 2 local blog posts",
            "• Add LocalBusiness schema markup",
            "• Embed Google Maps on contact page",
            "• Start weekly Google Posts (offers/updates)"
        ]),
        ("<b>Ongoing (Monthly):</b>", [
            "• Post 3-5 photos weekly on GBP",
            "• Collect 8-10 new reviews per month",
            "• Publish 2 local blog posts",
            "• Monitor Google Search Console",
            "• Track rankings with local rank tracker",
            "• Respond to reviews within 24 hours",
            "• Update hours for holidays/events"
        ]),
    ]
    
    for title, items in action_plan:
        story.append(Paragraph(title, subheading_style))
        for item in items:
            story.append(Paragraph(item, styles['Normal']))
        story.append(Spacer(1, 8))
    
    story.append(Spacer(1, 24))
    
    story.append(Paragraph("🎯 <b>Expected Results Timeline:</b>", styles['Normal']))
    story.append(Paragraph("• <b>Month 1:</b> Profile optimized, citations built, first reviews coming in<br/>• <b>Month 2:</b> Ranking improvements, 50-100 GMB views daily<br/>• <b>Month 3:</b> Consistent leads, 10-20 calls/week from Google<br/>• <b>Month 4-6:</b> Dominant rankings, 200-500 monthly leads", styles['Normal']))
    
    story.append(Spacer(1, 24))
    
    story.append(Paragraph("💡 <b>Need Help Getting Started?</b>", styles['Normal']))
    story.append(Paragraph("Local SEO can be overwhelming to implement alone. Our affordable coaching packages provide personalized guidance, done-for-you setups, and ongoing support perfect for Indian small businesses. Visit TractionSEO.com to learn more.", styles['Normal']))
    
    # Build PDF
    doc.build(story, onFirstPage=create_header_footer, onLaterPages=create_header_footer)
    print(f"✅ Created: {filename}")
    return filename

# ============================================================================
# Main execution
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("TractionSEO - Generating 3 Beautiful PDF Resources")
    print("="*60 + "\n")
    
    # Create all PDFs
    pdf1 = create_seo_audit_checklist()
    pdf2 = create_chatgpt_prompts()
    pdf3 = create_local_seo_blueprint()
    
    print("\n" + "="*60)
    print("✅ All PDFs Generated Successfully!")
    print("="*60)
    print(f"\n📁 Files created in ./resources/ directory:")
    print(f"   1. {pdf1}")
    print(f"   2. {pdf2}")
    print(f"   3. {pdf3}")
    print("\n🎉 Ready to use on TractionSEO website!\n")
