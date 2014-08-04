yaragen
=======

Attempt at a yara rules generator for classification of malware families.  This should be able to generate binary rules.

NOTE: This is still a WIP

Current plan is as follows
    - A Rules engine will find Generator classes that subclass the 'BaseGen' type.
    - Current classes of generators are
        - HeaderGens - Parse header data(at start of file usually), can add/remove
            regions of interest for other classes of 'BaseGens'
        - BinaryGens - Generate binary yara rules based on some form of binary 
            differencing, a max_size, min_size, ratio and fuzzy_len are provided
            for some control
        - StructGens - Parse structures that may not necessarily be in the header
        - TextGens - Generate rules from textual data
        
    - Rules should be returned using the YaraRule types so the generator knows
        how to manage them.
        - AsciiStringRule
        - WideAsciiStringRule
        - BinaryStringRule