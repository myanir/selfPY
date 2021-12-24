def amount_of_oranges(big_glass=10, small_glass=20):
    orange_result = small_glass+big_glass * 3
    kg_result = orange_result / 5
    print("today you'll need ", orange_result, "oranges")
    print("buy", kg_result, "kg of oranges")
    return orange_result, kg_result


# oranges_number, kg_oranges = amount_of_oranges(3, 5)
# print("oranges_number", oranges_number, "\nkg_oranges", kg_oranges)
amount_of_oranges(small_glass=3, big_glass=5) #call function with name and value
amount_of_oranges()

def func  (num1, num2):
     """Calculate Sum of 2 numbers
     :param num1: num1 value
     :param num2: num2 value
     :type num1: int
     :type num2: int
     :return: The result of the sum
     :rtype: int
     """
     c = num1 + num2
     return c

"""נסביר את מבנה התיעוד של הפונקציה:

בשורה 2 מתועדת בקצרה פעולת הפונקציה.
בהמשך התיעוד מתוארים הפרמטרים שהפונקציה מקבלת (אם יש כאלה), והערכים שהיא מחזירה. כל שורה נפתחת בנקודתיים.
בשורה 3 ובשורה 4 מופיע פירוט הפרמטרים שהפונקציה מקבלת. כל פרמטר שהפונקציה מקבלת מתועד בשורה נפרדת על ידי המילה param, שם הפרמטר ואחריו נקודתיים, והסבר על הפרמטר.
בשורה 5 ובשורה 6 מופיעים הטיפוסים של הפרמטרים. הטיפוסים של הפרמטרים מתועדים על ידי המילה type, שם הפרמטר (בהתאמה לשמות שתועדו קודם) ואחריו נקודתיים, וטיפוס הפרמטר. גם כאן, הטיפוס של כל פרמטר מתועד בשורה נפרדת.
בשורה 7 מופיע פירוט על הערכים שהפונקציה מחזירה. ערך ההחזרה מתועד על ידי המילה return, נקודתיים, והסבר על ערך ההחזרה.
שימו לב, אם אין בפונקציה שורת return שמחזירה ערך במפורש, נכתוב None בתיעוד ערך ההחזרה.
בשורה 8 מופיע טיפוס הערך המוחזר. הטיפוס מתועד על ידי המילה rtype ונקודתיים, וטיפוס הערך.

לאחר שתיעדנו פונקציה נוכל לצפות בתיעוד שלה.
זוכרים את הפונקציה func? כך נצפה בתיעוד שלה:
 
 help(func)
>>> """