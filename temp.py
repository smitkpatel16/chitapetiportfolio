import os
from random import shuffle
# <div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-books">
#     <div class="portfolio-content h-100">
#         <img src="assets/img/portfolio/books-3.jpg" class="img-fluid" alt="">
#         <div class="portfolio-info">
#             <h4>Books 3</h4>
#             <p>Lorem ipsum, dolor sit amet consectetur</p>
#             <a href="assets/img/portfolio/books-3.jpg" title="Branding 3"
#                 data-gallery="portfolio-gallery-book" class="glightbox preview-link"><i
#                     class="bi bi-zoom-in"></i></a>
#             <a href="portfolio-details.html" title="More Details" class="details-link"><i
#                     class="bi bi-link-45deg"></i></a>
#         </div>
#     </div>
# </div><!-- End Portfolio Item -->
f = open("portolio-part.html", "w")
assets_dir = os.path.join('assets', 'portfolio')
categories = []
category_counts = {}
htmlcontainers = []
for root, dirs, files in os.walk(assets_dir):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
            rel_dir = os.path.relpath(root, assets_dir)
            category = rel_dir.split(
                os.sep)[0] if rel_dir != '.' else 'uncategorized'
            if category not in categories:
                categories.append(category)
            # # Limit to 20 per category
            count = category_counts.get(category, 0)
            # if count >= 20:
            #     # # Move file to temp folder if limit exceeded
            #     # temp_dir = os.path.join('temp')
            #     # # os.makedirs(temp_dir, exist_ok=True)
            #     # src_path = os.path.join(root, file)
            #     # dst_path = os.path.join(temp_dir, file)
            #     # os.rename(src_path, dst_path)
            #     continue
            category_counts[category] = count + 1

            filter_class = f'filter-{category.lower()}'
            img_path = os.path.join(
                'assets', 'portfolio', rel_dir, file).replace('\\', '/')
            html = f'''
<div class="col-lg-4 col-md-6 portfolio-item isotope-item {filter_class}">
    <div class="portfolio-content h-100">
        <img src="{img_path}" class="img-fluid" alt="">
        <div class="portfolio-info">
            <h4>{category.title()}</h4>
            <p>{file}</p>
            <a href="{img_path}" title="{category.title()}" data-gallery="portfolio-gallery-{category.lower()}" class="glightbox preview-link"><i class="bi bi-zoom-in"></i></a>
            <a href="portfolio-details.html" title="More Details" class="details-link"><i class="bi bi-link-45deg"></i></a>
        </div>
    </div>
</div><!-- End Portfolio Item -->
'''
            htmlcontainers.append(html)
shuffle(htmlcontainers)
for html in htmlcontainers:
    f.write(html)

f.close()
for category in categories:
    print(f'<li data-filter=".filter-{category.lower()}">{category}</li>')
