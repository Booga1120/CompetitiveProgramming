# Competitive Programming Workflow

Quick setup for solving problems with easy testing and submission.

## 📁 Structure

```
competitive_programming/
├── templates/
│   ├── java/
│   │   ├── Solution.java
│   │   └── test.sh
│   └── javascript/
│       ├── solution.js
│       └── test.sh
├── problem_name_java/
│   ├── Solution.java    # Code here (with packages, no errors)
│   ├── submission.txt   # Auto-generated for Kattis
│   ├── samples/
│   │   ├── 1.in, 1.ans
│   │   └── 2.in, 2.ans
│   └── test.sh
└── problem_name_js/
    ├── solution.js      # Code here 
    ├── submission.txt   # Auto-generated for Kattis
    ├── samples/
    └── test.sh
```

## 🚀 Setup New Problem

### Java
```bash
cp -r templates/java/ problem_name_java/
cd problem_name_java/
chmod +x test.sh
mkdir samples
# Add your .in and .ans files to samples/
```

### JavaScript  
```bash
cp -r templates/javascript/ problem_name_js/
cd problem_name_js/
chmod +x test.sh
mkdir samples
# Add your .in and .ans files to samples/
```

## 🔄 Workflow

1. **Code** in `Solution.java` or `solution.js` (development files with full IDE support)
2. **Test** with `./test.sh` (auto-generates `submission.txt`)
3. **Submit** by copying `submission.txt` contents to Kattis

## 📋 Test Output

```
Compiled ✓

Test 1:
  In:  I love ba-na-na
  Out: Gah kove bababa
  Exp: Gah kove bababa
  ✓ PASS

submission.txt ready for Kattis!
```

## ✅ Key Points

- Always code in development files (`Solution.java` or `solution.js`)
- Never edit `submission.txt` (auto-generated)
- Development files have proper packages/structure (no IDE errors)
- `test.sh` handles all conversion and testing
- Copy template folders for new problems