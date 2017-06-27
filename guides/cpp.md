---
layout: page
permalink: /cplusplus/
title: C++ Nuggets
tags: [c++]
comments: false
---

This page is (or better: will become) a collection of C++ features I find useful and worthy to share!

### Use emplace() instead of push()
If you ever browsed throught the list of functions at cplusplus.com (the best online reference I know of) you might have seen that c++11 adds the 'emplace()' function to most of STL's containers. What is is and why is it useful?

First of all, it produces the same result as push() (e.g. push_back() for vectors).
But it does it more efficently and by that I mean faster!

Why's that? Consider the following example:

```c++
std::vector<std::string> vs;
vs.push_back("this is not a string");
```

Since "this is not a string" is not a string (ha) but a ```const char[21]```, c++ will first call a constructor like this:
```c++
vs.push_back(st::string("this is not a string"));
```

This involves a call to the string constructor (and later to its destructor) and then again another call to a constructor when the new string object is finally pushed into the vector.

On the other side, we have:

```c++
vs.emplace_back("this is not a string");
```

skips all the intermediate constructors/destructors and immediatly forwards the data into the vector, so that the string constructor is called only once. Much faster, so good.


Also here is a nice video of Scott Meyer at "NDC'14" talking about Modern Effective Modern C++:


[![Scott Meyers](http://img.youtube.com/vi/IqVZG6jWXvs/0.jpg)](https://vimeo.com/97318797 "Scott Meyers - Modern Effective C++")
