#!/usr/bin/env ruby

require 'imdb_party'

class MovieManager
  def initialize(movie)
    puts "Welcome to Cyprus"
    @movie = movie
    @imdb = ImdbParty::Imdb.new
  end

  def lookup()
    puts "Looking up #{@movie}"
    movie = @imdb.find_by_title(@movie)
    puts
    if movie.empty?
      puts "Movie not found."
    else
      puts "Title: #{movie[0][:title]}"
      puts "Year: #{movie[0][:year]}"
      puts "Poster URL #{movie[0][:poster_url]}"
    end
  end
end
