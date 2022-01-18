SELECT
	authors.id,
	authors.name,
	paper_authors.author_id,
	paper_authors.paper_id,
	papers.id,
	papers.year as publish_year,
	papers.title as paper_title,
	papers.pdf_name,
	papers.abstract as paper_abstract,
	papers.paper_text
FROM paper_authors
INNER JOIN papers ON paper_authors.paper_id = papers.id
INNER JOIN authors ON paper_authors.author_id = authors.id;
	