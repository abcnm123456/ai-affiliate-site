---
layout: home
title: AI 工具評測網
permalink: /
---

<section class="hero">
  <h1>🤖 找到最適合你的 AI 工具</h1>
  <p>專業評測、即時更新、幫你做出最好選擇</p>
</section>

<section class="features">
  <div class="feature">
    <span class="icon">📊</span>
    <h3>深度評測</h3>
    <p>每款工具都經過實際測試與詳細分析</p>
  </div>
  <div class="feature">
    <span class="icon">⚡</span>
    <h3>每日更新</h3>
    <p>AI 領域變化快速，我們每天為你追蹤</p>
  </div>
  <div class="feature">
    <span class="icon">💰</span>
    <h3>省錢推薦</h3>
    <p>獨家優惠碼與最佳性價比方案</p>
  </div>
</section>

<section class="latest-posts">
  <h2>最新評測文章</h2>
  <div class="post-grid">
    {% for post in site.posts limit:6 %}
    <article class="post-card">
      <span class="post-date">{{ post.date | date: "%Y/%m/%d" }}</span>
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      <p>{{ post.excerpt | strip_html | truncate: 100 }}</p>
      <a href="{{ post.url }}" class="read-more">閱讀更多 →</a>
    </article>
    {% endfor %}
  </div>
</section>

<section class="newsletter">
  <h2>📬 訂閱更新通知</h2>
  <p>輸入郵箱，第一時間收到新評測文章</p>
  <form class="subscribe-form" action="#" method="post">
    <input type="email" placeholder="your@email.com" required>
    <button type="submit">訂閱</button>
  </form>
</section>

<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; color: #333; }
  
  .hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 4rem 2rem;
    text-align: center;
  }
  .hero h1 { font-size: 2.5rem; margin-bottom: 1rem; }
  .hero p { font-size: 1.2rem; opacity: 0.9; }
  
  .features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    padding: 3rem 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }
  .feature { text-align: center; padding: 1.5rem; }
  .feature .icon { font-size: 3rem; display: block; margin-bottom: 1rem; }
  .feature h3 { color: #667eea; margin-bottom: 0.5rem; }
  
  .latest-posts { max-width: 1200px; margin: 0 auto; padding: 2rem; }
  .latest-posts h2 { margin-bottom: 1.5rem; color: #333; }
  
  .post-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
  }
  .post-card {
    background: #f8f9fa;
    border-radius: 12px;
    padding: 1.5rem;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .post-card:hover { transform: translateY(-4px); box-shadow: 0 8px 20px rgba(0,0,0,0.1); }
  .post-date { font-size: 0.85rem; color: #666; }
  .post-card h3 { margin: 0.5rem 0; }
  .post-card h3 a { color: #333; text-decoration: none; }
  .post-card p { color: #666; font-size: 0.95rem; }
  .read-more { display: inline-block; margin-top: 1rem; color: #667eea; text-decoration: none; font-weight: 600; }
  
  .newsletter {
    background: #f0f4ff;
    padding: 3rem 2rem;
    text-align: center;
    margin-top: 2rem;
  }
  .newsletter h2 { color: #667eea; }
  .newsletter p { margin: 0.5rem 0 1.5rem; }
  .subscribe-form { display: flex; justify-content: center; gap: 0.5rem; flex-wrap: wrap; }
  .subscribe-form input { padding: 0.8rem 1rem; border: 2px solid #ddd; border-radius: 8px; font-size: 1rem; min-width: 250px; }
  .subscribe-form button {
    padding: 0.8rem 2rem;
    background: #667eea;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.2s;
  }
  .subscribe-form button:hover { background: #764ba2; }
  
  @media (max-width: 600px) {
    .hero h1 { font-size: 1.8rem; }
    .features { padding: 2rem 1rem; }
  }
</style>
