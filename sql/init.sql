CREATE DATABASE IF NOT EXISTS hive_results;
USE hive_results;
CREATE TABLE IF NOT EXISTS hive_results.summary (
    country VARCHAR(255) PRIMARY KEY,
    user_count INT NOT NULL
);