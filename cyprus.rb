#!/usr/bin/env ruby

require File.join(File.dirname(__FILE__), "moviemanager.rb")

if __FILE__ == $0
  ARGV.each do |a|
    cp = MovieManager.new(a)
    cp.lookup
  end
end
