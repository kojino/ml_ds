class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception

  def urls
    # render html: 'hello world'

    if params[:search]
      @users = ExternalCustomer.search(params[:search]).order("shared_at DESC")
    else
      @users = ExternalCustomer.all.order('shared_at DESC')
    end
  end
end
