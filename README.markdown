# Cyprus

Cyprus is a movie library management application currently in development
and written in Python.

Cyprus is designed to be very easy to use. A configuration file is placed in
~/.cyprus/config, and at first run it's automatically generated. In this file
a directory is marked as your library, and cyprus will copy movie files you 
run it against into this directory. Cyprus names the directory and file 
properly, and even pulls a .tbn thumbnail for use with XBMC.

Here's an example of cyprus in action:

    $ cyprus "Inception.mkv"
    Search term: Inception

	Movie
	=====
	Title: Inception (2010)
	Genres: Action, Crime, Mystery, Sci-Fi, Thriller.
	Director: Christopher Nolan.
	Writer: Christopher Nolan.
	Cast: Leonardo DiCaprio (Cobb), Joseph Gordon-Levitt (Arthur),
        Ellen Page (Ariadne), Tom Hardy (Eames), Ken Watanabe (Saito).
	Runtime: 148.
	Country: USAUK.
	Language: English, Japanese, French.
	Rating: 9.0 (283428 votes).
	Plot: Dom Cobb is a skilled thief, the absolute best in the dangerous art
    of extraction, stealing valuable secrets from deep within the subconscious
    during the dream state, when the mind is at its most vulnerable. Cobb's
    rare ability has made him a coveted player in this treacherous new world
    of corporate espionage, but it has also made him an international fugitive
    and cost him everything he has ever loved. Now Cobb is being offered a 
    chance at redemption. One last job could give him his life back but only
    if he can accomplish the impossible-inception. Instead of the perfect 
    heist, Cobb and his team of specialists have to pull off the reverse:
    their task is not to steal an idea but to plant one. If they succeed,
    it could be the perfect crime. But no amount of careful planning or
    expertise can prepare the team for the dangerous enemy that seems to
    predict their every move. An enemy that only Cobb could have seen 
    coming.
	
	Is this movie correct? Y/N: y
	Movie is correct. Copying to library...
	[ #################################################################### ] 100% 

In testing, Cyprus generally gets movies right on the first try. If something
causes an incorrect result, Cyprus will list other potential results, and will
ask for a custom search term if all else fails:

	Is this movie correct? Y/N: n
	
	Printing other results: 
	1 Inception
	2 Inception: 4Movie Premiere Special
	3 Inception: Motion Comics
	4 WWA: The Inception
	5 The Inception
	Correct movie (or N for none): n
	Please provide new search term: Some Other Movie! 

Cyprus also supports batch operations. Throw a bunch of movies together in a
single folder and use shell expansion:

    [sensae@europa][0]$ ./cyprus testmovies/*
    {'verbose': False}
	Looking up file testmovies/2001 A Space Odyssey.mkv...
	2001 A Space Odyssey (1968)
	Is this mov correct? Y/N: y
	Movie is correct. Copying to library...
	[ #################################################################### ] 100% 
	
	Looking up file testmovies/Inception.mkv...
	Inception (2010)
	Is this mov correct? Y/N: y
	Movie is correct. Copying to library...
	[ #################################################################### ] 100% 
	
	Looking up file testmovies/The Informant.mkv...
	Informant!, The (2009)
	Is this mov correct? Y/N: y
	Movie is correct. Copying to library...
	[ #################################################################### ] 100% 
	
	[sensae@europa][0]$ 
	
