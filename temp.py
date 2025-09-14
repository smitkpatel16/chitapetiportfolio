import os

'''
<div class = "col-lg-4 col-md-6 portfolio-item isotope-item filter-wedding" >
   <div class = "portfolio-content h-100" >
        <img src = "assets/portfolio/Wedding/pre wedding/_MG_3940_Original.jpg" class = "img-fluid" alt = "" >
        <div class = "portfolio-info" >
            <h4 > Wedding < /h4 >
            <p > _MG_3940_Original.jpg < /p >
            <a href = "assets/portfolio/Wedding/pre wedding/_MG_3940_Original.jpg" title = "Wedding" data-gallery = "portfolio-gallery-wedding" class = "glightbox preview-link" > <i class = "bi bi-zoom-in" > </i > </a >
            <a href = "portfolio-details.html" title = "More Details" class = "details-link" > <i class = "bi bi-link-45deg" > </i > </a >
        </div >
    </div >
</div > <!-- End Portfolio Item - ->
'''


def generate_portfolio_items(base_dir="assets/portfolio"):
    html_sections = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                rel_dir = os.path.relpath(root, base_dir)
                category = rel_dir.split(
                    os.sep)[0] if os.sep in rel_dir else rel_dir
                category_class = f"filter-{category.lower().replace(' ', '-')}"
                img_path = os.path.join(root, file).replace("\\", "/")
                html = f'''
<div class="col-lg-4 col-md-6 portfolio-item isotope-item {category_class}">
   <div class="portfolio-content h-100">
        <img src="{img_path}" class="img-fluid" alt="">
        <div class="portfolio-info">
            <h4>{category}</h4>
            <p>{file}</p>
            <a href="{img_path}" title="{category}" data-gallery="portfolio-gallery-{category.lower()}" class="glightbox preview-link"><i class="bi bi-zoom-in"></i></a>
            <a href="portfolio-details.html" title="More Details" class="details-link"><i class="bi bi-link-45deg"></i></a>
        </div>
    </div>
</div>
'''
                html_sections.append(html)
    return "\n".join(html_sections)


ps = generate_portfolio_items()
with open("portfolio-section.html", "w", encoding="utf-8") as f:
    f.write(ps)
