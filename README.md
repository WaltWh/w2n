# Word to Number

This is a Python module to convert number words (e.g. twenty-one) to numeric digits (21). It works for positive numbers
up through the quinvigintillions (10^78) - i.e. the maximum value is 10^81 - 1, a number which I will not clutter this
readme with in either a fully spelled-out or decimal form.

This version of the module has no dependencies. However, it has only been tested on Python 3.10.
## Installation

Please ensure that you have **updated pip** to the latest version before installing word2number.

You can install the module using Python Package Index using the below command.

    pip install https://github.com/WaltWh/w2n/tarball/1.2

(Note that you can also put it in your requirements.txt file that way. Just drop that whole URL in as its own line.)

## Usage

First you have to import the module:

    import w2n

### word_to_num

You can use the `word_to_num` method to convert a number-word to numeric digits, as shown below.

```python
print(w2n.word_to_num("two million three thousand nine hundred and eighty four"))
2003984
```

```python
print(w2n.word_to_num('two point three'))
2.3
```

```python
print(w2n.word_to_num('112'))
112
```

```python
print(w2n.word_to_num('point one'))
0.1
```

```python
print(w2n.word_to_num('one hundred thirty-five'))
135
```

```python
print(w2n.word_to_num('million million'))
# Error: Redundant number! Please enter a valid number word (eg. two million twenty three thousand and forty nine)
None
```

```python
print(w2n.word_to_num('blah'))
# Error: No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)
None
```

### numwords_in_sentence

You can also use the `numwords_in_sentence` function to convert numbers within a text string to digits in-place.

```python
print(w2n.numwords_in_sentence(
    'A hundred and twelve years, two hundred and twenty-one days, thirteen hours, and twenty-two minutes'))
'112 years, 221 days, 13 hours, and 22 minutes'
```

## Bugs/Errors

There are known bugs around lists of numbers; these could reasonably be considered 'undefined behavior' for
`word_to_num` but are admittedly undesired for `numwords_in_sentence`. Resolving these may require more in-depth NLP
capabilities and is currently considered to be beyond the scope of this package. Pull requests are welcome.

```python
print(w2n.word_to_num("one thousand, two hundred, and three"))
1203
# for word_to_num, this must be correct, as it accepts only one number per string
print(w2n.numwords_in_sentence("one thousand, two hundred, and three"))
'1203'
# for numwords_in_sentence, though, '1000, 200, 3' could also be the intended value
```

```python
print(w2n.word_to_num('five, twenty-three, seven'))
35
# Should technically be a ValueError, but not totally unreasonable as 'undefined behavior do not use'
print(w2n.numwords_in_sentence('five, twenty-three, seven'))
'35'
# Yeah, this should definitely be '5, 23, 7'
```

Please ensure that you have updated pip to the latest version before installing word2number.

If you find any bugs/errors in the usage of above code, please raise an issue
through [Github](https://github.com/WaltWh/w2n). If you don't know how to use Github or raise an issue through it, I
suggest that you should learn it. Else, send an email to tinman@mage.city with a clear example that can reproduce the
issue.

## Contributors

- Ben Batorsky [bpben](https://github.com/bpben)
- Alex [ledovsky](https://github.com/ledovsky)
- Tal Yarkoni [tyarkoni](https://github.com/tyarkoni)
- ButteredGroove [ButteredGroove](https://github.com/ButteredGroove)

## License

License is available in LICENSE.txt. It's the MIT license.
