🐍 Python Log Parser
A high-performance Python log parser built to handle gigabyte-sized log files efficiently using generators and memory-friendly techniques. Ideal for parsing large logs without loading them entirely into memory.

🚀 Features
Line-by-line processing using generators

Minimal memory footprint

Supports custom filters and pattern matching

Easy to integrate into larger data pipelines

🛠 Installation
Clone the repository:
```git clone https://github.com/nikpirat/python-log-parser.git```
```cd python-log-parser```

▶️ Usage
```python log_parser.py /path/to/your/large-log-file.log```
You can customize parsing behavior (e.g. filters or output) by modifying the log_parser.py script or passing CLI arguments (if implemented).

📁 Example
```python log_parser.py ./logs/server.log --filter ERROR --output errors.txt```

Advantages:

1. Memory Efficiency
Traditional approach:
Tools like pandas.read_csv() or reading the whole file with readlines() can load the entire file into memory.
For a 2 GB log file, this could consume multiple gigabytes of RAM.

Generator-based approach:
Processes one log line at a time using generators (yield), meaning:
Memory usage stays constant, regardless of file size.
Typical RAM usage: under 100 MB, even for multi-GB files.
Can run on low-resource machines (e.g. a Raspberry Pi or cloud function).

2. Clean Separation of Concerns
Each module (reader, parser, filter, writer) handles one responsibility.
Easy to extend, test, or replace parts (e.g., change from CSV output to database insertion).

3. Performance Gains (Scalable I/O)
I/O bottlenecks are minimized due to:
Buffered reading with file iterators.
No intermediate large objects created (e.g., huge lists).
You could process millions of lines per minute, depending on disk and CPU.

Benchmarks (Estimates)
Input Size	Traditional (pandas/readlines)	Your App (generators)
1 GB	    ~1–2 GB RAM usage	            ~20–50 MB RAM
5 GB	    Often crashes or swaps	        Still ~20–50 MB RAM
10M lines	~20–30 sec	                    ~5–10 sec (no full load)

Tips:
Use memory-mapped files (mmap) if random access is needed.
Avoid pandas for initial parsing on GB-scale logs—it loads data into memory.
Use lazy evaluation wherever possible (i.e., yield, map(), filter()).
Parallel processing (optional): Use multiprocessing or concurrent.futures if CPU-bound and safe.
