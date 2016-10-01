json.extract! user, :id, :first_name, :last_name, :email, :role, :about_me, :skill, :contact, :admin, :created_at, :updated_at
json.url user_url(user, format: :json)