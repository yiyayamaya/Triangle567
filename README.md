# Triangle567

___

testing the initial classifyTriangle() implementation

| Test ID            | Input         |  Expected Results   |  Actual Result   |  Pass or Fail   |
|--------------------|---------------|-----|-----|-----|
| testInvalidInput1  | "3", "", ""   |  "InvalidInput"   |  Error   |   Error  |
| testInvalidInput2  | -1, -1, -1    |  "InvalidInput"   |   "InvalidInput"  |  Pass   |
| testInvalidInput3  | 999, 999, 999 |  "InvalidInput"   |   "InvalidInput"  |  Pass   |
| testRightTriangle1 | 3, 4, 5       |  "Right"   |   "InvalidInput"  |  Fail   |
| testRightTriangle2 | 50, 30, 40    |  "Right"   |   "InvalidInput"  |  Fail   |
| testNotTriangle1 | 1, 1, 2       |  "NotATriangle"   |   "InvalidInput"  |  Fail   |
| testNotTriangle1 | 1, 1, 3       |  "NotATriangle"   |   "InvalidInput"  |  Fail   |
| testIsoceles1 | 2, 2, 3       |  "Isoceles"   |   "InvalidInput"  |  Fail   |
| testEquilateral1 | 2, 2, 2       |  "Equilateral"   |   "InvalidInput"  |  Fail   |
| testScalene1 | 2, 3, 4       |  "Scalene"   |   "InvalidInput"  |  Fail   |


___
testing the improved classifyTriangle() implementation

| Test ID            | Input         |  Expected Results   |  Actual Result   |  Pass or Fail   |
|--------------------|---------------|-----|-----|-----|
| testInvalidInput1  | "3", "", ""   |  "InvalidInput"   |  "InvalidInput"   |   Pass  |
| testInvalidInput2  | -1, -1, -1    |  "InvalidInput"   |   "InvalidInput"  |  Pass   |
| testInvalidInput3  | 999, 999, 999 |  "InvalidInput"   |   "InvalidInput"  |  Pass   |
| testRightTriangle1 | 3, 4, 5       |  "Right"   |   "Right"  |  Pass   |
| testRightTriangle2 | 50, 30, 40    |  "Right"   |   "Right"  |  Pass   |
| testNotTriangle1 | 1, 1, 2       |  "NotATriangle"   |   "NotATriangle"  |  Pass   |
| testNotTriangle1 | 1, 1, 3       |  "NotATriangle"   |   "NotATriangle"  |  Pass   |
| testIsoceles1 | 2, 2, 3       |  "Isoceles"   |   "Isoceles"  |  Pass   |
| testEquilateral1 | 2, 2, 2       |  "Equilateral"   |   "Equilateral"  |  Pass   |
| testScalene1 | 2, 3, 4       |  "Scalene"   |   "Scalene"  |  Pass   |

___
