from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.models import User  # استيراد نموذج المستخدم

def add_user(session: Session, username, email, password, role, first_name, last_name, phone_number):
    """إضافة مستخدم جديد مع التحقق من البريد الإلكتروني ورقم الهاتف"""
    
    # التحقق من وجود المستخدم مسبقًا
    user_exists = session.query(User.id).filter(
        (User.email == email) | (User.phone_number == phone_number)
    ).scalar()

    if user_exists:
        return {"error": "البريد الإلكتروني أو رقم الهاتف مسجل بالفعل. الرجاء استخدام بيانات مختلفة."}

    # تشفير كلمة المرور
    from werkzeug.security import generate_password_hash
    hashed_password = generate_password_hash(password)

    # إنشاء مستخدم جديد
    new_user = User(
        username=username,
        email=email,
        password_hash=hashed_password,  # تأكد من حفظ كلمة المرور المشفرة
        role=role,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number
    )

    try:
        session.add(new_user)
        session.commit()
        return {"message": "تمت إضافة المستخدم بنجاح"}
    except IntegrityError as e:
        session.rollback()

        # التحقق من سبب الخطأ لمعرفة هل هو تعارض في UNIQUE
        if "unique_email" in str(e.orig):
            return {"error": "البريد الإلكتروني مسجل بالفعل."}
        elif "unique_phone_number" in str(e.orig):
            return {"error": "رقم الهاتف مسجل بالفعل."}
        else:
            return {"error": "حدث خطأ أثناء إضافة المستخدم. حاول مرة أخرى لاحقًا."}
    finally:
        session.close()  # إغلاق الجلسة بعد التنفيذ
