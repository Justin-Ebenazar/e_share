from flask import Flask,render_template,request,redirect,flash,send_file
import pymysql as ps
from io import BytesIO
from base64 import b64encode
import binascii

app=Flask(__name__)


con=ps.connect(host="localhost",user="root",password="12345678",database="e_waste",cursorclass=ps.cursors.DictCursor)

cursor=con.cursor()
username=0
password=0

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html" ,info={})

@app.route('/sign_in',methods=['POST','GET'])
def sign_in():
    global username,password
    if(request.method=='POST'):
        user_name=request.form.get('user_n')
        pass_word=request.form.get('pass')
        print(user_name,pass_word,123,sep="-")
        cursor.execute(f"select * from login_credentials  where username='{user_name}' and p_word='{pass_word}'")
        data=cursor.fetchall()
        if(len(data)!=0):
            username=user_name
            password=pass_word
            return redirect("/home")
        else:
            return render_template("index.html",info={},cred="w_signin")

@app.route('/new_ac',methods=['POST','GET'])
def new_ac():
    first_n=request.form['f_name']
    last_n=request.form['l_name']
    user_n=request.form.get('new_u_name')
    print(user_n)
    cursor.execute(f"select * from login_credentials where username= '{user_n}'")
    iruku_illa=cursor.fetchall()

    new_pass=request.form['new_pass']
    mobile=int(request.form['mob'])
    loc=request.form['Location']
    if(len(iruku_illa)!=0):
        user_n="Try another"
        print("already iruku")
        print(iruku_illa,123)
        
        return render_template('index.html',info={'f_n':first_n,'l_n':last_n,'user_n':user_n,'new_pass':"","mobile":mobile,"loc":loc},mic="iruku")
    else:
        try:
            cursor.execute(f"insert into login_credentials values('{user_n}','{new_pass}','{first_n}','{last_n}',{mobile},'{loc}')")
            con.commit()
            flash("hello world")
        except Exception as e:
            print(e)
        return render_template('index.html',info={'f_n':first_n,'l_n':last_n,'user_n':user_n,'new_pass':"","mobile":mobile,"loc":loc},mic="illa")

@app.route('/post_ad', methods=['POST', 'GET'])
def post_ad():
    global username
    if request.method == 'POST':
        try:
            # Get text data
            checkboxes = request.form.getlist('chek')
            custom_text = request.form.get('cust_text')
            desc=request.form.get('description')

            # Insert text data into posts table
            cursor.execute("INSERT INTO posts (username, components, descript, sold) VALUES (%s, %s, %s, %s)", 
                           (username, ','.join(checkboxes)+ custom_text,desc, "no"))
            con.commit()
            # Retrieve the generated post_id
            post_id = cursor.lastrowid
            print("inga thaa error")
            # Get image data
            images = request.files.getlist('images[]')
            blobs = []
            mime_types = []
            for img in images:
                blobs.append(img.read())
                mime_types.append(img.mimetype)

            # Insert image data into images table
            for i, j in zip(blobs, mime_types):
                cursor.execute("INSERT INTO images (post_id, img, mime) VALUES (%s, %s, %s)", 
                               (post_id, i, j))
                con.commit()

            return redirect('/home')
        except Exception as e:
            print(f"Error: {e}")
            return "Error nadanthathu"

    elif request.method == 'GET':
        return "cute"


@app.route('/home')
def home():
    global username
    try:
        cursor.execute(f"SELECT p.post_id, p.username, p.components, p.descript, hex(i.img) as img, i.mime,l.loca FROM posts p JOIN images i ON p.post_id = i.post_id inner join login_credentials l on p.username=l.username WHERE p.username != '{username}' ORDER BY p.post_id DESC LIMIT 6")
    except:
        print("etho error iruku")
    posts = cursor.fetchall()
    for post in posts:
        # Process each post and its corresponding image
        post.update({'img':b64encode(binascii.unhexlify(post['img'])).decode('utf-8').replace('\r', '').replace(u'\xa0', ' ').replace('¶', '')})

    return render_template('home.html',info=posts)

@app.route('/search_item',methods=['POST','GET'])
def search_item():
    if request.method == 'POST':
        print('ulle vanthathu')
        search_value = request.form['SEARCHVALUE']
        filter = request.form['FILTER']
        cursor.execute(f"SELECT p.post_id, p.username, p.components, p.descript, hex(i.img) as img, i.mime,l.loca FROM posts p JOIN images i ON p.post_id = i.post_id inner join login_credentials l on p.username=l.username WHERE p.username != '{username}' AND components like '%{search_value}%'")
        posts = cursor.fetchall()
        for post in posts:
        # Process each post and its corresponding image
            post.update({'img':b64encode(binascii.unhexlify(post['img'])).decode('utf-8').replace('\r', '').replace(u'\xa0', ' ').replace('¶', '')})

        return render_template('home.html',info=posts)

@app.route('/view_post/<int:post_id>')
def view_post(post_id):
    cursor.execute("SELECT p.components, p.descript, l.loca ,l.mobile FROM posts p INNER JOIN login_credentials l ON p.username = l.username WHERE p.post_id = %s", (post_id,))
    post_details = cursor.fetchone()
    cursor.execute(f"select hex(img) as img,mime from images where post_id='{post_id}'")
    iamge=cursor.fetchall()
    for i in iamge:
        i.update({'img':b64encode(binascii.unhexlify(i['img'])).decode('utf-8').replace('\r', '').replace(u'\xa0', ' ').replace('¶', '')})
    return render_template('result.html', post_details=post_details,images=iamge)

if __name__=="__main__":
    app.secret_key="admin480"
    app.run(debug=True)
