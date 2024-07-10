# Report for Assignment 1 Resit

**Name:** Whisper  
**URL:** [https://github.com/openai/whisper](https://github.com/openai/whisper)  
**Number of lines of code and the tool used to count it:** 19,576 (Counted using [codetabs](https://codetabs.com/count-loc/count-loc-online.html))  
**Programming language:** Python  
**Coverage Tool used:** coverage.py

![Coverage Tool](Picture1.jpg)  

## Coverage Improvement

### 1. Tokenizer

- **Commit made:** [8d3ded0353247f7e951f04de646e4c7f610e57d5](https://github.com/openai/whisper/commit/8d3ded0353247f7e951f04de646e4c7f610e57d5)
- **Old coverage:** ![Old Coverage Tokenizer](Picture2.jpg)
- **New coverage:** ![New Coverage Tokenizer](Picture3.jpg)
- **Improvement:** The coverage improved by 11% by adding test cases for:
  - Encoding
  - Decoding
  - Unknown language
  - Splitting

### 2. Audio

- **Commit made:** [a5ee907d7315160d1747aedc55b5ada7b6ec964a](https://github.com/openai/whisper/commit/a5ee907d7315160d1747aedc55b5ada7b6ec964a)
- **Old coverage:** ![Old Coverage Audio](Picture4.jpg)
- **New coverage:** ![New Coverage Audio](Picture5.jpg)
- **Improvement:** The coverage improved by 29% by adding test cases for:
  - When the device is set
  - When padding is defined
  - The `pad_or_trim` function when sizes are smaller or larger than `N_SAMPLE`

## Overall Coverage

1. **Old overall coverage:** ![Old Overall Coverage](Picture6.jpg)
2. **New overall coverage:** ![New Overall Coverage](Picture7.jpg)
