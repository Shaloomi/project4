drop table rental_info;


-- Create Rental Table
CREATE TABLE rental_info (
  id INT PRIMARY KEY NOT NULL,
    posted_on Date,
    bhk INT,
    rent INT,
    size INT,
    floor VARCHAR(100),
    area_type VARCHAR(100),
    area_locality VARCHAR(100),
    city VARCHAR(50),
    furnishing_status VARCHAR(50),
    tenant_preferred VARCHAR(50),
    bathroom INT,
    point_of_contact VARCHAR(50)
);


select * from rental_info