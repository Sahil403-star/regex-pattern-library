# Regex Pattern Library (Real-World Data Extraction)

## Why I built this

While working on receipt parsing, I noticed most regex examples online are too clean and unrealistic.
In real scenarios (especially OCR, logs, and emails), the data is messy, inconsistent, and full of edge cases.

So instead of solving textbook problems, I built this repository to practice regex on **real-world-like inputs** and understand its limitations.

---

## What I focused on

* Handling OCR issues like `T0tal`, `Tot al`
* Supporting both formatted and unformatted numbers (`1,299` vs `1299`)
* Writing patterns that are flexible but not too loose
* Improving patterns after seeing failure cases
* Understanding when regex is NOT the right tool

---

## Example

**Input:**

```
T0tal ₹1,2 9 9
```

**Output:**

```
1299
```

---

## Approach I followed

I didn’t try to write a perfect regex from the start.

* Started with simple patterns
* Tested on messy inputs
* Noticed failures (wrong matches, missed cases)
* Iteratively improved patterns

In some files, I’ve also left comments about what didn’t work initially.

---

## Key challenges faced

* OCR noise (extra spaces, wrong characters)
* Multiple formats for the same data
* Overly strict regex failing valid cases
* Overly loose regex matching invalid data

---

## Engineering decisions

* Used **hybrid patterns** to balance strictness and flexibility
* Added **normalization step** (removing commas, cleaning spaces)
* Included **invalid test cases** intentionally
* Avoided over-optimizing patterns without testing

---

## Folder structure

```
problems/     -> basic real-world regex problems  
advanced/     -> validation + tricky cases  
datasets/     -> messy input samples  
```

---

## Limitations

* Regex struggles with highly unstructured or multi-line layouts
* Nested HTML parsing is unreliable → better handled using XPath
* Some patterns still fail for extreme OCR noise

---

## What I learned

Regex is not just about matching patterns.

It’s about:

* understanding the data
* handling inconsistencies
* and knowing when to stop relying on regex

---

## Future improvements

* Add a preprocessing layer before the regex
* Try rule-based + ML hybrid approach
* Integrate with OCR tools for end-to-end parsing

---

## Note

Some patterns in this repo were intentionally improved over time after testing on edge cases.
This reflects how parsing problems evolve in real scenarios.

---

