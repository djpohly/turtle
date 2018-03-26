# Turtle redux

This program creates a Python-based turtle graphics environment intended
specifically for those who are learning to program for the first time.  Most of
the functionality is provided by the [turtle
module](https://docs.python.org/3.3/library/turtle.html), but a few language
features have been added or borrowed from Logo where the Python syntax was
deemed non-obvious to a beginner.

To enter an interactive environment, simply run

    $ ./turtle

All of the functions of the turtle module are available at the top level, so
you may simply type something like:

    >>> fd(100)
    >>> rt(90)
    >>> fd(100)
    >>> lt(90)

and so on.

A "turtle script" in an external file may also be run non-interactively, in
which case execution will pause when the program finishes, and the interpreter
will exit as soon as the turtle window is closed.  To run a script in this way,
pass the name of the file on the command line, as in:

    $ ./turtle stars

Scripts may be given a ".py" extension to aid text editors in choosing
appropriate syntax coloring and indentation.  The interpreter will attempt to
find the filename as specified or with the extension added (i.e., the above
example will look first for a file called "stars", then for one called
"stars.py" if that is not found).


# Language additions/amendments

## New language blocks

### filled

The `filled` block encapsulates the `begin_fill`, `end_fill`, and `fillcolor`
functions from the original module.  It provides an intuitive way to introduce
block syntax without needing any algorithmic concepts (such as loops or
conditionals).  The syntax of this block is:

    filled <color>:
        ...

where *<color>* is a string such as `"yellow"`, `"steelblue"` or `"#002664"`.
(As implementation currently also permits three comma-separated floats,
although we have opted to focus on a single syntax in the classroom and lab.)

A `filled` block may not be nested inside another `filled` since the turtle
module does not provide intuitive results when attempting to nest fills.

### repeat

Logo's `repeat` loop has been ported for use in a way which is consistent with
Python syntax:

    repeat 5:
        forward(100)
	left(144)

(Rationale: `for _ in range(N)` is not immediately obvious or comprensible even
to programmers coming from other languages, let alone to complete programming
beginners.)

As in Logo, a loop counter which begins counting at 1 is accessible via the
variable `repcount`:

    repeat 100:
        forward(repcount)
	right(20)

### forever

The `forever` loop from Logo was also ported, though we have not introduced it
in teaching.  Ctrl-C may still be used to interrupt these loops or other
runaway code.

### to

Logo defines new functions using a `to` statement which is similar enough to
Python's `def` for easy translation.  Functions with arguments are created
using parentheses as in Python, but the parentheses may be omitted for
functions without arguments.

    # Here's to you, Logo
    to square:
        repeat 4:
	    fd(100)
	    rt(90)

(Rationale: less technical-sounding and intimidating than `def`?  Probably more
nostalgia than anything, to be honest.)


## New functions

### random()

The `random` function takes a single integer n and returns a random integer
between 1 and n inclusive.

### randomcolor()

The `randomcolor` function returns a triple of random values between 0.0 and
1.0, suitable for passing to `pencolor` or `filled`.

### wait()

The `wait` function has been ported from Logo; it sleeps for the given amount
of time, measured in tenths of a second.  For example, `wait(30)` pauses
execution for three seconds.

### load()

The `load` function takes the name of a file (with or without a trailing ".py")
and executes it in the turtle context.  This allows students to define
functions in a separate file that may be reused in multiple places without
needing to understand modules.

This can also be used to run a source file during an interactive session for
debugging or experimentation.


## Additional abbreviations

Some commands have been given new abbreviations or aliases:

* `cs`: `clearscreen`
* `ps`: `pensize`
* `pc`: `pencolor`
* `bg`: `bgcolor`
* `arc`: `circle`

The alias for `circle` was added to avoid having to address the concept of
optional arguments.  Students were told that the `circle` command takes one
parameter and draws a circle, and that the `arc` command takes two parameters
and draws an arc.


# Known issues

* Closing the turtle window in non-interactive mode results in a
  turtle.Terminator being raised and another window being opened.  This should
  probably exit the interpreter instead.
* Syntax parsing on the arguments to new blocks is not perfect.  In particular,
  expressions which include a colon will likely break the syntax.
* Ctrl-C is not caught immediately when typing a command.  This is,
  unfortunately, a problem with Tkinter and not something cleanly fixable from
  our code.  (A hack exists that may be applied in the future, or sooner if a
  patch is submitted.)
