class ExternalUrl < ActiveRecord::Base
  establish_connection :external_url_table
  table_name "urls"
end
