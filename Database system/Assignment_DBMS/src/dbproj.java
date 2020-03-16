import java.sql.*;
import java.util.Scanner;

public class dbproj {
    
    private static int menu = 0, usermenu = 0, mgrmenu = 0, userssn = 0, mgrssn = 0, amount = 0;
    private static long account = 0, get_account = 0;
    private static Date loan_term;
    private static float loan_interest;
    private static Scanner keyboard = new Scanner(System.in);
    private static Connection con = null;
    private static Statement stmt = null;
    private static ResultSet rs = null;
    
    public static int menu() {
        
        System.out.println("0. Exit");
        System.out.println("1. User Menu");
        System.out.println("2. Manager Menu");
        System.out.print("Input : ");
        
        int temp = keyboard.nextInt();
        
        return temp;
    }
    public static int userMenu() {
        
        System.out.println("0. Return to previous menu");
        System.out.println("1. View account");
        System.out.println("2. REMITTANCE");
        System.out.println("3. DEPOSIT");
        System.out.println("4. WITHDRAW");
        System.out.println("5. LOAN");
        System.out.println("6. View transaction history");
        System.out.println("7. Make an account");
        System.out.println("8. Remove an account");
        System.out.print("Input : ");
        
        int temp = keyboard.nextInt();
        
        return temp;
    }
    public static int userSsn() {
        
        System.out.print("User ssn : ");
        
        int temp = keyboard.nextInt();
        
        return temp;
    }
    public static long account() {
        
        System.out.print("Account : ");
        
        long temp = keyboard.nextLong();
        
        return temp;
    }
    public static long getting_account() {
        
        System.out.print("Getting_account : ");
        
        long temp = keyboard.nextLong();
        
        return temp;
    }
    public static int amount() {
        
        System.out.print("Amount : ");
        
        int temp = keyboard.nextInt();
        
        return temp;
    }
    public static Date term() {
        
        System.out.print("Term(20xx-xx-xx) : ");
        
        String temp = keyboard.next();
        
        Date temp2 = Date.valueOf(temp);
        
        return temp2;
    }
    public static float interest() {
        
        System.out.print("Interest(1.xx) : ");
        
        float temp = keyboard.nextFloat();
        
        return temp;
    }
    public static int mgrMenu() {
        
        System.out.println("0. Return to previous menu");
        System.out.println("1. View all users' transaction history");
        System.out.println("2. View a user's transaction history");
        System.out.println("3. View all users' account");
        System.out.println("4. View a user's account");
        System.out.print("Input : ");
        
        int temp = keyboard.nextInt();
        
        return temp;
    }
    public static int mgrSsn() {
        
        System.out.print("Manager ssn : ");
        
        int temp = keyboard.nextInt();
        
        return temp;
    }
    public static void main(String[] args) {
        try {
            
            con = DriverManager.getConnection("jdbc:mariadb://localhost:3306/bank", "jinkyo422", "qkqhek123");
            
            stmt = con.createStatement();
            
            while(true) {
                menu = menu();
                
                if(menu == 0)    break;
                
                else if(menu == 1) {
                    while(true) {
                        usermenu = userMenu();
                        
                        if(usermenu == 0)    break;
                        
                        else if(usermenu == 1) {
                            
                            userssn = userSsn();
                            
                            rs = stmt.executeQuery( "select * from account where ussn=" + userssn);
                            
                            System.out.println("*If term is null and interest is 0.0, account is ordinary deposit.");
                            System.out.println("*If not, account is time deposit.");
                            System.out.println("--------------------------------------------");
                            System.out.println("   anumber  \tbalance\t   term\t\tinterest");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                long anumber = rs.getLong(1);
                                long balance = rs.getLong(2);
                                Date term = rs.getDate(3);
                                float interest = rs.getFloat(4);
                                if(term == null) {
                                    System.out.println(anumber + "\t" + balance + "\t   " + term + "\t\t" + interest);
                                }
                                else{
                                    System.out.println(anumber + "\t" + balance + "\t   " + term + "\t" + interest);
                                }
                            }
                            System.out.println("--------------------------------------------");
                            rs.close();
                        }
                        else if(usermenu == 2) {
                            
                            userssn = userSsn();
                            account = account();
                            
                            Date term = null, term2 = null;
                            int balance = -1, balance2 = -1;
                            
                            rs = stmt.executeQuery("select balance, term from account where anumber=" + account
                                                   + " and ussn=" + userssn);
                            
                            if(rs.next()) {
                                balance = rs.getInt(1);
                                term = rs.getDate(2);
                            }
                            if(balance == -1) {
                                System.out.println("*The account does not exist");
                                rs.close();
                                continue;
                            }
                            if(term != null) {
                                System.out.println("*The account is time deposit.");
                                rs.close();
                                continue;
                            }
                            
                            get_account = getting_account();
                            
                            rs = stmt.executeQuery("select balance, term from account where anumber=" + get_account);
                            
                            if(rs.next()) {
                                balance2 = rs.getInt(1);
                                term2 = rs.getDate(2);
                            }
                            if(balance2 == -1) {
                                System.out.println("*The getting account does not exist");
                                rs.close();
                                continue;
                            }
                            if(term2 != null) {
                                System.out.println("*The getting account is time deposit.");
                                rs.close();
                                continue;
                            }
                            
                            amount = amount();
                            
                            if(balance < amount) {
                                System.out.println("*There is no money in the account.");
                                rs.close();
                                continue;
                            }
                            
                            rs = stmt.executeQuery("select ssn from manager");
                            if(rs.next())    mgrssn = rs.getInt(1);
                            
                            int rnumber = 0;
                            rs = stmt.executeQuery("select max(rnumber) from remittance");
                            if(rs.next())        rnumber = rs.getInt(1);
                            rnumber++;
                            
                            stmt.executeUpdate("insert into remittance values('"
                                               + rnumber + "','" + amount +  "','" + get_account + "','"
                                               + account + "','" + mgrssn + "')");
                            
                            balance = balance - amount;
                            stmt.executeUpdate("update account set balance=" + balance
                                               + " where anumber=" + account);
                            
                            balance2 = balance2 + amount;
                            stmt.executeUpdate("update account set balance=" + balance2
                                               + " where anumber=" + get_account);
                            
                            System.out.println("*REMITTANCE success!");
                            rs.close();
                        }
                        else if(usermenu == 3) {
                            
                            userssn = userSsn();
                            account = account();
                            
                            Date term = null;
                            int balance = -1;
                            
                            rs = stmt.executeQuery("select balance, term from account where anumber="
                                                   + account + " and ussn=" + userssn);
                            
                            if(rs.next()) {
                                balance = rs.getInt(1);
                                term = rs.getDate(2);
                            }
                            if(balance == -1) {
                                System.out.println("*The account does not exist");
                                rs.close();
                                continue;
                            }
                            if(term != null) {
                                System.out.println("*The account is time deposit.");
                                rs.close();
                                continue;
                            }
                            
                            amount = amount();
                            
                            rs = stmt.executeQuery("select ssn from manager");
                            if(rs.next())    mgrssn = rs.getInt(1);
                            
                            int dnumber = 0;
                            rs = stmt.executeQuery("select max(dnumber) from deposit");
                            if(rs.next())        dnumber = rs.getInt(1);
                            dnumber++;
                            
                            stmt.executeUpdate("insert into deposit values('"
                                               + dnumber + "','" + amount + "','" + account + "','" + mgrssn
                                               + "')");
                            
                            balance = balance + amount;
                            stmt.executeUpdate("update account set balance=" + balance
                                               + " where anumber=" + account);
                            
                            System.out.println("*DEPOSIT success!");
                            rs.close();
                        }
                        else if(usermenu == 4) {
                            
                            userssn = userSsn();
                            account = account();
                            
                            Date term = null;
                            int balance = -1;
                            
                            rs = stmt.executeQuery("select balance, term from account where anumber=" + account
                                                   + " and ussn=" + userssn);
                            
                            if(rs.next()) {
                                balance = rs.getInt(1);
                                term = rs.getDate(2);
                            }
                            if(balance == -1) {
                                System.out.println("*The account does not exist");
                                rs.close();
                                continue;
                            }
                            if(term != null) {
                                System.out.println("*The account is time deposit.");
                                rs.close();
                                continue;
                            }
                            
                            amount = amount();
                            
                            if(balance < amount) {
                                System.out.println("*There is no money in the account.");
                                rs.close();
                                continue;
                            }
                            
                            rs = stmt.executeQuery("select ssn from manager");
                            if(rs.next())    mgrssn = rs.getInt(1);
                            
                            int wnumber = 0;
                            rs = stmt.executeQuery("select max(wnumber) from withdraw");
                            if(rs.next())        wnumber = rs.getInt(1);
                            wnumber++;
                            
                            stmt.executeUpdate("insert into withdraw values('"
                                               + wnumber + "','" + amount + "','" + account + "','" + mgrssn
                                               + "')");
                            
                            balance = balance - amount;
                            stmt.executeUpdate("update account set balance=" + balance
                                               + " where anumber=" + account);
                            
                            System.out.println("*WITHDRAW success!");
                            rs.close();
                        }
                        else if(usermenu == 5) {
                            
                            userssn = userSsn();
                            
                            int loan = 0;
                            
                            rs = stmt.executeQuery("select lnumber from account, loan where ussn = " + userssn
                                                   + " and laccount = anumber");
                            
                            if(rs.next()) {
                                loan = rs.getInt(1);
                            }
                            if(loan != 0) {
                                System.out.println("*You already have a loan");
                                rs.close();
                                continue;
                            }
                            
                            account = account();
                            
                            Date term = null;
                            int balance = -1;
                            
                            rs = stmt.executeQuery("select balance, term from account where anumber=" + account
                                                   + " and ussn=" + userssn);
                            
                            if(rs.next()) {
                                balance = rs.getInt(1);
                                term = rs.getDate(2);
                            }
                            if(balance == -1) {
                                System.out.println("*The account does not exist");
                                rs.close();
                                continue;
                            }
                            if(term != null) {
                                System.out.println("*The account is time deposit.");
                                rs.close();
                                continue;
                            }
                            
                            loan_term = term();
                            loan_interest = interest();
                            amount = amount();
                            
                            rs = stmt.executeQuery("select ssn from manager");
                            if(rs.next())    mgrssn = rs.getInt(1);
                            
                            int lnumber = 0;
                            rs = stmt.executeQuery("select max(lnumber) from loan");
                            if(rs.next())        lnumber = rs.getInt(1);
                            lnumber++;
                            
                            stmt.executeUpdate("insert into loan values('"
                                               + lnumber + "','" + amount + "','" + loan_term + "','" + loan_interest + "','" +
                                               account + "','" + mgrssn + "')");
                            
                            balance = balance + amount;
                            stmt.executeUpdate("update account set balance=" + balance
                                               + " where anumber=" + account);
                            
                            System.out.println("*LOAN success!");
                            rs.close();
                        }
                        else if(usermenu == 6) {
                            
                            userssn = userSsn();
                            
                            System.out.println("*REMITTANCE history");
                            rs = stmt.executeQuery( "select ramount, getting_account, raccount from account, remittance "
                                                   + "where anumber = raccount and ussn=" + userssn);
                            
                            System.out.println("--------------------------------------------");
                            System.out.println("   anumber  \tamount\t   getting_account");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                long anumber = rs.getLong(3);
                                int amount = rs.getInt(1);
                                long getting_account = rs.getLong(2);
                                System.out.println(anumber + "\t" + amount + "\t   " + getting_account);
                            }
                            System.out.println("--------------------------------------------");
                            
                            System.out.println("*Getting history");
                            rs = stmt.executeQuery( "select ramount, getting_account, raccount from account, remittance "
                                                   + "where anumber = getting_account and ussn=" + userssn);
                            
                            System.out.println("--------------------------------------------");
                            System.out.println("   anumber  \tamount\t   sent_account");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                long anumber = rs.getLong(2);
                                int amount = rs.getInt(1);
                                long sent_account = rs.getLong(3);
                                System.out.println(anumber + "\t" + amount + "\t   " + sent_account);
                            }
                            System.out.println("--------------------------------------------");
                            
                            
                            System.out.println("*DEPOSIT history");
                            rs = stmt.executeQuery( "select damount, daccount from account, deposit "
                                                   + "where anumber = daccount and ussn=" + userssn);
                            
                            System.out.println("--------------------------------------------");
                            System.out.println("   anumber  \tamount\t   ");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                long anumber = rs.getLong(2);
                                int amount = rs.getInt(1);
                                System.out.println(anumber + "\t" + amount);
                            }
                            System.out.println("--------------------------------------------");
                            
                            System.out.println("*WITHDRAW history");
                            rs = stmt.executeQuery( "select wamount, waccount from account, withdraw "
                                                   + "where anumber = waccount and ussn=" + userssn);
                            
                            System.out.println("--------------------------------------------");
                            System.out.println("   anumber  \tamount\t   ");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                long anumber = rs.getLong(2);
                                int amount = rs.getInt(1);
                                System.out.println(anumber + "\t" + amount);
                            }
                            System.out.println("--------------------------------------------");
                            
                            System.out.println("*LOAN history");
                            rs = stmt.executeQuery( "select lamount, lterm, linterest, laccount from account, loan "
                                                   + "where anumber = laccount and ussn=" + userssn);
                            
                            System.out.println("--------------------------------------------");
                            System.out.println("   anumber  \tamount\t   term\t\tinterest");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                long anumber = rs.getLong(4);
                                int amount = rs.getInt(1);
                                Date term = rs.getDate(2);
                                float interest = rs.getFloat(3);
                                System.out.println(anumber + "\t" + amount + "\t   " + term + "\t" + interest);
                            }
                            System.out.println("--------------------------------------------");
                            rs.close();
                        }
                        else if(usermenu == 7) {
                            
                            userssn = userSsn();
                            
                            int salary = 0;
                            
                            rs = stmt.executeQuery("select salary from user where ssn=" + userssn);
                            
                            if(rs.next())    salary = rs.getInt(1);
                            if(salary == 0) {
                                System.out.println("*The user does not exist.");
                                rs.close();
                                continue;
                            }
                            System.out.println("*Account number must be 12 digits.");
                            
                            account = account();
                            int lenth = (int)(Math.log10(account)+1);
                            
                            if(lenth != 12) {
                                System.out.println("*The account number is not 12 digits.");
                                rs.close();
                                continue;
                            }
                            
                            int balance = -1;
                            
                            rs = stmt.executeQuery("select balance from account where anumber=" + account);
                            
                            if(rs.next())    balance = rs.getInt(1);
                            if(balance != -1) {
                                System.out.println("*The account number already exists.");
                                rs.close();
                                continue;
                            }
                            
                            String temp = "2020-1-1";
                            loan_term = Date.valueOf(temp);
                            loan_interest = (float) 1.01;
                            
                            System.out.println("*You can make a time deposit or an ordinary deposit.");
                            System.out.println("*A time depoisit : term is " + loan_term + " and interest is " + loan_interest);
                            System.out.println("*If you want, T or t. If not, O or o");
                            System.out.print("Account type : ");
                            
                            String type = keyboard.next();
                            
                            if(type.equals("T") || type.equals("t")) {
                                System.out.println("*How much do you want?");
                                System.out.print("Money : ");
                                balance = keyboard.nextInt();
                                
                                rs = stmt.executeQuery("select ssn from manager");
                                if(rs.next())    mgrssn = rs.getInt(1);
                                
                                int dnumber = 0;
                                rs = stmt.executeQuery("select max(dnumber) from deposit");
                                if(rs.next())        dnumber = rs.getInt(1);
                                dnumber++;
                                
                                stmt.executeUpdate("insert into account values('"
                                                   + account + "','" + balance +  "','" + loan_term + "','" + loan_interest + "','" + userssn
                                                   + "')");
                                
                                stmt.executeUpdate("insert into deposit values('"
                                                   + dnumber + "','" + balance + "','" + account + "','" + mgrssn
                                                   + "')");
                                
                                System.out.println("*Success to make a time deposit!");
                            }
                            else if(type.equals("O") || type.equals("o")){
                                stmt.executeUpdate("insert into account values('"
                                                   + account + "','0', null, null,'" + userssn
                                                   + "')");
                                System.out.println("*Success to make a ordinary deposit!");
                            }
                            else {
                                System.out.println("Input Error..");
                            }
                            rs.close();
                        }
                        else if(usermenu == 8) {
                            
                            userssn = userSsn();
                            
                            int salary = 0;
                            
                            rs = stmt.executeQuery("select salary from user where ssn=" + userssn);
                            
                            if(rs.next())    salary = rs.getInt(1);
                            if(salary == 0) {
                                System.out.println("*The user does not exist.");
                                rs.close();
                                continue;
                            }
                            System.out.println("*Do you want to remove your account?");
                            System.out.println("*Although it is a time deposit, you cannot take the interest");
                            System.out.println("*If you want, Y or y. If not, N or n");
                            System.out.print("Answer: ");
                            
                            String ans = keyboard.next();
                            
                            if(ans.equals("Y") || ans.equals("y")) {
                                System.out.println("*Which account do you want to remove?");
                                account = account();
                                
                                int balance = -1;
                                
                                rs = stmt.executeQuery("select balance from account where anumber=" + account
                                                       + " and ussn=" + userssn);
                                
                                if(rs.next())    balance = rs.getInt(1);
                                
                                if(balance == -1) {
                                    System.out.println("*The account does not exist.");
                                    continue;
                                }
                                
                                int lnumber = 0;
                                
                                rs = stmt.executeQuery("select lnumber from loan where laccount = " + account);
                                
                                if(rs.next())    lnumber = rs.getInt(1);
                                
                                if(lnumber != 0) {
                                    System.out.println("*The account has a loan.");
                                    continue;
                                }
                                
                                stmt.executeUpdate("delete from remittance where rnumber="+ account);
                                stmt.executeUpdate("delete from remittance where getting_account="+ account);
                                stmt.executeUpdate("delete from deposit where dnumber="+ account);
                                stmt.executeUpdate("delete from withdraw where wnumber="+ account);
                                stmt.executeUpdate("delete from account where anumber="+ account);
                                System.out.println("*You take " + balance + ".");
                                System.out.println("*Success to remove the account!");
                            }
                            else if(ans.equals("N") || ans.equals("n")) {
                                System.out.println("*It's a good choice.");
                            }
                            else {
                                System.out.println("Input Error..");
                            }
                            rs.close();
                        }
                        else {
                            System.out.println("Input Error..");
                        }
                    }
                }
                
                else if(menu == 2) {
                    while(true) {
                        mgrmenu = mgrMenu();
                        
                        if(mgrmenu == 0)        break;
                        
                        else if(mgrmenu == 1) {
                            
                            mgrssn = mgrSsn();
                            
                            int salary = 0;
                            
                            rs = stmt.executeQuery("select salary from manager where ssn=" + mgrssn);
                            
                            if(rs.next())    salary = rs.getInt(1);
                            if(salary == 0) {
                                System.out.println("You are not manager.");
                                rs.close();
                                continue;
                            }
                            
                            System.out.println("*REMITTANCE history");
                            rs = stmt.executeQuery( "select name, ssn, ramount, getting_account, raccount"
                                                   + " from user, account, remittance "
                                                   + " where anumber = raccount and ussn=ssn");
                            
                            System.out.println("--------------------------------------------");
                            System.out.println("name\t ssn\t\tanumber  \tamount\t   getting_account");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                String name = rs.getString(1);
                                int ssn = rs.getInt(2);
                                long anumber = rs.getLong(5);
                                int amount = rs.getInt(3);
                                long getting_account = rs.getLong(4);
                                System.out.println(name + "\t " + ssn + "\t" + anumber + "\t" + amount + "\t   " + getting_account);
                            }
                            System.out.println("--------------------------------------------");
                            
                            System.out.println("*Getting history");
                            rs = stmt.executeQuery( "select name, ssn, ramount, getting_account, raccount"
                                                   + " from user, account, remittance "
                                                   + " where anumber = getting_account and ussn=ssn");
                            
                            System.out.println("--------------------------------------------");
                            System.out.println("name\t ssn\t\tanumber  \tamount\t   sent_account");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                String name = rs.getString(1);
                                int ssn = rs.getInt(2);
                                long anumber = rs.getLong(4);
                                int amount = rs.getInt(3);
                                long sent_account = rs.getLong(5);
                                System.out.println(name + "\t " + ssn + "\t" + anumber + "\t" + amount + "\t   " + sent_account);
                            }
                            System.out.println("--------------------------------------------");
                            
                            System.out.println("*DEPOSIT history");
                            rs = stmt.executeQuery( "select name, ssn, damount, daccount "
                                                   + " from user, account, deposit "
                                                   + " where anumber = daccount and ussn=ssn");
                            
                            System.out.println("--------------------------------------------");
                            System.out.println("name\t ssn\t\tanumber  \tamount\t   ");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                String name = rs.getString(1);
                                int ssn = rs.getInt(2);
                                long anumber = rs.getLong(4);
                                int amount = rs.getInt(3);
                                System.out.println(name + "\t " + ssn + "\t" + anumber + "\t" + amount);
                            }
                            System.out.println("--------------------------------------------");
                            
                            System.out.println("*WITHDRAW history");
                            rs = stmt.executeQuery( "select name, ssn, wamount, waccount "
                                                   + " from user, account, withdraw "
                                                   + " where anumber = waccount and ussn=ssn");
                            
                            System.out.println("--------------------------------------------");
                            System.out.println("name\t ssn\t\tanumber  \tamount\t   ");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                String name = rs.getString(1);
                                int ssn = rs.getInt(2);
                                long anumber = rs.getLong(4);
                                int amount = rs.getInt(3);
                                System.out.println(name + "\t " + ssn + "\t" + anumber + "\t" + amount);
                            }
                            System.out.println("--------------------------------------------");
                            
                            System.out.println("*LOAN history");
                            rs = stmt.executeQuery( "select name, ssn, lamount, lterm, linterest, laccount "
                                                   + " from user, account, loan "
                                                   + " where anumber = laccount and ussn=ssn");
                            
                            System.out.println("--------------------------------------------");
                            System.out.println("name\t ssn\t\tanumber  \tamount\t   term\t\tinterest");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                String name = rs.getString(1);
                                int ssn = rs.getInt(2);
                                long anumber = rs.getLong(6);
                                int amount = rs.getInt(3);
                                Date term = rs.getDate(4);
                                float interest = rs.getFloat(5);
                                System.out.println(name + "\t " + ssn + "\t" + anumber + "\t" + amount + "\t   " + term + "\t" + interest);
                            }
                            System.out.println("--------------------------------------------");
                            rs.close();
                        }
                        else if(mgrmenu == 2) {
                            
                            mgrssn = mgrSsn();
                            
                            int salary = 0;
                            
                            rs = stmt.executeQuery("select salary from manager where ssn=" + mgrssn);
                            
                            if(rs.next())    salary = rs.getInt(1);
                            if(salary == 0) {
                                System.out.println("You are not manager.");
                                rs.close();
                                continue;
                            }
                            
                            userssn = userSsn();
                            
                            salary = 0;
                            
                            rs = stmt.executeQuery("select salary from user where ssn=" + userssn);
                            
                            if(rs.next())    salary = rs.getInt(1);
                            if(salary == 0) {
                                System.out.println("The user does not exist.");
                                rs.close();
                                continue;
                            }
                            
                            System.out.println("*REMITTANCE history");
                            rs = stmt.executeQuery( "select name, ramount, getting_account, raccount "
                                                   + " from user, account, remittance "
                                                   + " where anumber = raccount and ussn=ssn and ssn=" + userssn);
                            
                            System.out.println("--------------------------------------------");
                            System.out.println("name\t anumber  \tamount\t   getting_account");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                String name = rs.getString(1);
                                long anumber = rs.getLong(4);
                                int amount = rs.getInt(2);
                                long getting_account = rs.getLong(3);
                                System.out.println(name + "\t " + anumber + "\t" + amount + "\t   " + getting_account);
                            }
                            System.out.println("--------------------------------------------");
                            
                            System.out.println("*Getting history");
                            rs = stmt.executeQuery( "select name, ssn, ramount, getting_account, raccount"
                                                   + " from user, account, remittance "
                                                   + " where anumber = getting_account and ussn=ssn and ssn=" + userssn);
                            
                            System.out.println("--------------------------------------------");
                            System.out.println("name\t anumber  \tamount\t   sent_account");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                String name = rs.getString(1);
                                long anumber = rs.getLong(2);
                                int amount = rs.getInt(3);
                                long sent_account = rs.getLong(4);
                                System.out.println(name + "\t " + anumber + "\t" + amount + "\t   " + sent_account);
                            }
                            System.out.println("--------------------------------------------");
                            
                            System.out.println("*DEPOSIT history");
                            rs = stmt.executeQuery( "select name, damount, daccount from user, account, deposit "
                                                   + "where anumber = daccount and ussn=ssn and ssn=" + userssn);
                            
                            System.out.println("--------------------------------------------");
                            System.out.println("name\t anumber  \tamount\t   ");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                String name = rs.getString(1);
                                long anumber = rs.getLong(3);
                                int amount = rs.getInt(2);
                                System.out.println(name + "\t " + anumber + "\t" + amount);
                            }
                            System.out.println("--------------------------------------------");
                            
                            System.out.println("*WITHDRAW history");
                            rs = stmt.executeQuery( "select name, wamount, waccount from user, account, withdraw "
                                                   + "where anumber = waccount and ussn=ssn and ssn=" + userssn);
                            
                            System.out.println("--------------------------------------------");
                            System.out.println("name\t anumber  \tamount\t   ");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                String name = rs.getString(1);
                                long anumber = rs.getLong(3);
                                int amount = rs.getInt(2);
                                System.out.println(name + "\t " + anumber + "\t" + amount);
                            }
                            System.out.println("--------------------------------------------");
                            
                            System.out.println("*LOAN history");
                            rs = stmt.executeQuery( "select name, lamount, lterm, linterest, laccount "
                                                   + " from user, account, loan "
                                                   + " where anumber = laccount and ussn=ssn and ssn=" + userssn);
                            
                            System.out.println("--------------------------------------------");
                            System.out.println("name\t anumber  \tamount\t   term\t\tinterest");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                String name = rs.getString(1);
                                long anumber = rs.getLong(5);
                                int amount = rs.getInt(2);
                                Date term = rs.getDate(3);
                                float interest = rs.getFloat(4);
                                System.out.println(name + "\t " + anumber + "\t" + amount + "\t   " + term + "\t" + interest);
                            }
                            System.out.println("--------------------------------------------");
                            rs.close();
                        }
                        else if(mgrmenu == 3) {
                            
                            mgrssn = mgrSsn();
                            
                            int salary = 0;
                            
                            rs = stmt.executeQuery("select salary from manager where ssn=" + mgrssn);
                            
                            if(rs.next())    salary = rs.getInt(1);
                            if(salary == 0) {
                                System.out.println("You are not manager.");
                                rs.close();
                                continue;
                            }
                            
                            rs = stmt.executeQuery( "select name, ssn, anumber, balance, term, interest"
                                                   + " from user, account where ussn=ssn");
                            
                            System.out.println("*If term is null and interest is 0.0, account is ordinary deposit.");
                            System.out.println("*If not, account is time deposit.");
                            System.out.println("--------------------------------------------");
                            System.out.println("name\t ssn\t\tanumber  \tbalance\t   term\t\tinterest");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                String name = rs.getString(1);
                                int ssn = rs.getInt(2);
                                long anumber = rs.getLong(3);
                                long balance = rs.getLong(4);
                                Date term = rs.getDate(5);
                                float interest = rs.getFloat(6);
                                if(term == null) {
                                    System.out.println(name + "\t " + ssn + "\t" + anumber + "\t" + balance + "\t   "
                                                       + term + "\t\t" + interest);
                                }
                                else{
                                    System.out.println(name + "\t " + ssn + "\t" + anumber + "\t" + balance + "\t   "
                                                       + term + "\t" + interest);
                                }
                            }
                            System.out.println("--------------------------------------------");
                            rs.close();
                        }
                        else if(mgrmenu == 4) {
                            
                            mgrssn = mgrSsn();
                            
                            int salary = 0;
                            
                            rs = stmt.executeQuery("select salary from manager where ssn=" + mgrssn);
                            
                            if(rs.next())    salary = rs.getInt(1);
                            if(salary == 0) {
                                System.out.println("You are not manager.");
                                rs.close();
                                continue;
                            }
                            
                            userssn = userSsn();
                            
                            salary = 0;
                            
                            rs = stmt.executeQuery("select salary from user where ssn=" + userssn);
                            
                            if(rs.next())    salary = rs.getInt(1);
                            if(salary == 0) {
                                System.out.println("The user does not exist.");
                                rs.close();
                                continue;
                            }
                            
                            rs = stmt.executeQuery( "select name, anumber, balance, term, interest"
                                                   + " from user, account where ussn=ssn and ssn = " + userssn);
                            
                            System.out.println("*If term is null and interest is 0.0, account is ordinary deposit.");
                            System.out.println("*If not, account is time deposit.");
                            System.out.println("--------------------------------------------");
                            System.out.println("name\t anumber  \tbalance\t   term\t\tinterest");
                            System.out.println("--------------------------------------------");
                            while( rs.next() ) {
                                String name = rs.getString(1);
                                long anumber = rs.getLong(2);
                                long balance = rs.getLong(3);
                                Date term = rs.getDate(4);
                                float interest = rs.getFloat(5);
                                if(term == null) {
                                    System.out.println(name + "\t " + anumber + "\t" + balance + "\t   "
                                                       + term + "\t\t" + interest);
                                }
                                else{
                                    System.out.println(name + "\t " + anumber + "\t" + balance + "\t   "
                                                       + term + "\t" + interest);
                                }
                            }
                            System.out.println("--------------------------------------------");
                            rs.close();
                        }
                        else {
                            System.out.println("Input Error..");
                        }
                    }
                }
                
                else {
                    System.out.println("Input Error..");
                }
            }
            
            stmt.close();
            con.close();
        }
        catch ( Exception e ) {
            e.printStackTrace();
        }
    }
}
