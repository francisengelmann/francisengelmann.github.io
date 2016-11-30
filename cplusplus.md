---
layout: cv
permalink: /cplusplus/
title: C++ Nuggets
tags: [about]
comments: true
---
This page is (or better: will become) a collection of small C++ snippets I found useful and worthy to share!

### emplace() instead of push()
If you ever browsed throught the list of functions at cplusplus.com (the best online reference I know of) you might have seen that c++11 adds the 'emplace()' function to most of the stl containers. What is that and why is it useful?

First of all, it produces in the same result as push() (e.g. push_back() for vectors).
But, it does it more efficently, and by that I mean faster!

Why's that? Consider the following example:

std::vector<std::string> vs;
vs.push_back("this is not a string");

Since "this is not a string" is not a string (ha) but a const char[21], c++ will first call a constructor like this:
vs.push_back(st::string("this is not a string"));

This involves a call to the string constructor (and later to the destructor) and then again another call to a constructor when we add the new string object to the vector.

vs.emplace_black("this is not a string")

skips all the constructors/destructors in between an immediatly forwards the data into the vector, so that the string constractor is called only once. Much faster, so good. 



Aslo here is a nice video of Scott Meyer at "NDC'14" talking about Effective Modern C++:
https://vimeo.com/97318797
