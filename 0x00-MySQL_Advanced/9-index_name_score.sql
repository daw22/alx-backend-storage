-- creates an Index for name and score fields
CREATE INDEX idx_name_first_score
ON names (name(1), score);
