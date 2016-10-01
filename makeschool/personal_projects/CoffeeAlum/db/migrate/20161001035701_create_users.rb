class CreateUsers < ActiveRecord::Migration[5.0]
  def change
    create_table :users do |t|
      t.string :first_name
      t.string :last_name
      t.string :email
      t.string :role
      t.text :about_me
      t.text :skill
      t.text :contact
      t.boolean :admin

      t.timestamps
    end
  end
end
