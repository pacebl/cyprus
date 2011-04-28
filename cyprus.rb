#!/usr/bin/env ruby

require 'imdb_party'

class Cyprus
  def initialize(movie)
    puts "Welcome to Cyprus"
    @movie = movie
  end

  def lookup()
    puts "Looking up #{@movie}"
  end
end

cp = Cyprus.new "Inception"
cp.lookup
