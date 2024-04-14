-- Enable CDC on the database
EXEC sys.sp_cdc_enable_db;

-- Enable CDC on the table
EXEC sys.sp_cdc_enable_table 
@source_schema = N'dbo', 
@source_name = N'customers', 
@role_name = NULL;

-- Verify CDC is enabled on the table
SELECT * FROM cdc.change_tables;
SELECT * FROM cdc.index_columns;
SELECT * FROM [cdc].[cdc_jobs]



-- Disable CDC on the table
EXEC sys.sp_cdc_disable_table 
@source_schema = N'dbo', 
@source_name = N'customers', 
@capture_instance = 'all';

-- Disable CDC on the database
EXEC sys.sp_cdc_disable_db;