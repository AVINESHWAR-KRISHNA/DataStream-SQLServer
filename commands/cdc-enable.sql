-- Enable CDC on the database
EXEC sys.sp_cdc_enable_db;

-- Enable CDC on the table
EXEC sys.sp_cdc_enable_table 
@source_schema = N'dbo', 
@source_name = N'customers', 
@role_name = NULL;



-- Disable CDC on the table
EXEC sys.sp_cdc_disable_table 
@source_schema = N'dbo', 
@source_name = N'customers', 
@capture_instance = 'all';

-- Disable CDC on the database
EXEC sys.sp_cdc_disable_db;