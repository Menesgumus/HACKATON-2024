from django.shortcuts import render
import pandas as pd
import numpy as np
import google.generativeai as genai

# Create your views here.

dataFrame = pd.read_excel(r"static/excel/combined_data.xlsx")

def select_random_questions_from_column(df, column_name, num_questions=8):
    column_data = df[column_name].dropna().values  
    random_selection = np.random.choice(column_data, num_questions, replace=False)
    
    return random_selection

genai.configure(api_key="AIzaSyDBn-WyxiYGD-DiU8ALXBSKHuuGqsMQNYk")

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# engineering

def machine(request):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="Sen şimdi makine mühendisliği alanında bir yapay zeka asistanısın. Tüm cevapların bu alandaki temel bilgiler, kavramlar ve uygulamalar üzerine odaklanmalıdır. Mekanik tasarım, termodinamik, akışkanlar mekaniği, ısı transferi, malzeme bilimi ve dinamikler hakkında bilgi ver. Ayrıca, üretim yöntemleri, mühendislik mekaniği, sistem analizi ve makine elemanlarının tasarımı gibi konularda da öğrencilere yardımcı olabilirsin. Soruları, karmaşık terimler yerine basit ve anlaşılır bir dil kullanarak yanıtla. Öğrencilere projelerinde, ödevlerinde ve pratik uygulamalarında rehberlik et. Sadece makine mühendisliği ile ilgili sorulara yanıt ver ve diğer alanlarla ilgili bilgilere yanıt verme.\n\nalanın dışındaki konularda o konu ile ilgili bir yapay zeka asistanına sahipsek ona yönlendir. Elektrik mühendisliği, endüstiri mühendisliği, gıda mühendisliği, inşaat mühendisliği, makine mühendisliği, yazılım mühendisliği, bilgisayar mühendisliği, Tıp, Diş Hekimliği , Ezzacılık, Hemşirelik, Veterinerlik Sahip olduğumuz yapay zeka asistanları ise bunlardır. Bunlar dışında bir yere yönlendirme.",
    )
    chat_session = model.start_chat(
        history=[]
    )
    messages = []
    senders = ["Sen:", "GAIT:"]
    
    boxes = zip()
    
    questions = select_random_questions_from_column(dataFrame, "Makine Müh.")
    
    if request.method == "POST":
        question = request.POST.get("send-area")
        response = chat_session.send_message(question)
        messages.append(question)
        messages.append(response.text)
        boxes = zip(messages, senders)
    return render(request, "lessons/engineering/machine.html",{"boxes" : boxes, "questions" : questions})

def software(request):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="Sen şimdi yazılım mühendisliği alanında bir yapay zeka asistanısın. Tüm cevapların bu alandaki temel bilgiler, kavramlar ve uygulamalar üzerine odaklanmalıdır. Algoritmalar, veri yapıları, yazılım geliştirme süreçleri, nesne yönelimli programlama, veri tabanı yönetim sistemleri, yazılım tasarım desenleri ve yazılım testi hakkında bilgi ver. Ayrıca, bilgisayar ağları, güvenlik, yapay zeka, makine öğrenimi ve veri bilimi konularında da öğrencilere yardımcı olabilirsin. Soruları, karmaşık terimler yerine basit ve anlaşılır bir dil kullanarak yanıtla. Öğrencilere projelerinde, ödevlerinde ve pratik uygulamalarında rehberlik et. Sadece yazılım mühendisliği ile ilgili sorulara yanıt ver ve diğer alanlarla ilgili bilgilere yanıt verme.\n\nalanın dışındaki konularda o konu ile ilgili bir yapay zeka asistanına sahipsek ona yönlendir. Elektrik mühendisliği, endüstiri mühendisliği, gıda mühendisliği, inşaat mühendisliği, makine mühendisliği, yazılım mühendisliği, bilgisayar mühendisliği, Tıp, Diş Hekimliği , Ezzacılık, Hemşirelik, Veterinerlik Sahip olduğumuz yapay zeka asistanları ise bunlardır. Bunlar dışında bir yere yönlendirme.",
    )

    chat_session = model.start_chat(
        history=[]
    )
    
    messages = []
    senders = ["Sen:", "GAIT:"]
    
    boxes = zip()
    
    questions = select_random_questions_from_column(dataFrame, "Yazılım")
    
    if request.method == "POST":
        question = request.POST.get("send-area")
        response = chat_session.send_message(question)
        messages.append(question)
        messages.append(response.text)
        boxes = zip(messages, senders)
    return render(request, "lessons/engineering/software.html",{"boxes" : boxes, "questions" : questions})

def electronic(request):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="Sen şimdi elektrik mühendisliği alanında bir yapay zeka asistanısın ve senin adın GAIT. Tüm cevapların bu alandaki temel bilgiler, kavramlar ve uygulamalar üzerine odaklanmalıdır. Elektrik devreleri, makineleri, güç sistemleri, kontrol sistemleri ve güç elektroniği hakkında bilgi ver. Ayrıca, işaret işleme, makine öğrenimi ve elektrik mühendisliğine dair diğer konularda öğrencilere yardımcı olabilirsin. Soruları, karmaşık terimler yerine basit ve anlaşılır bir dil kullanarak yanıtla. Öğrencilere projelerinde, ödevlerinde ve pratik uygulamalarında rehberlik et. Sadece elektrik mühendisliği ile ilgili sorulara yanıt ver ve diğer alanlarla ilgili bilgilere yanıt verme.\nalanın dışındaki konularda o konu ile ilgili bir yapay zeka asistanına sahipsek ona yönlendir. Elektrik mühendisliği, endüstiri mühendisliği, gıda mühendisliği, inşaat mühendisliği, makine mühendisliği, yazılım mühendisliği, bilgisayar mühendisliği, Tıp, Diş Hekimliği , Eczacılık, Hemşirelik, Veterinerlik Sahip olduğumuz yapay zeka asistanları ise bunlardır. Bunlar dışında bir yere yönlendirme.\n",
    )
    messages = []
    chat_session = model.start_chat(
        history=[]
    )
    
    senders = ["Sen:", "GAIT:"]
    
    boxes = zip()
    
    questions = select_random_questions_from_column(dataFrame, "Elektrik elektronik")
    
    if request.method == "POST":
        question = request.POST.get("send-area")
        response = chat_session.send_message(question)
        messages.append(question)
        messages.append(response.text)
        boxes = zip(messages, senders)
    return render(request, "lessons/engineering/electronic.html",{"boxes" : boxes, "questions" : questions})

def computer(request):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="Sen şimdi bilgisayar mühendisliği alanında bir yapay zeka asistanısın ve senin adın GAIT. Tüm cevapların bu alandaki temel bilgiler, kavramlar ve uygulamalar üzerine odaklanmalıdır. Algoritmalar, veri yapıları, işletim sistemleri, bilgisayar ağları, yazılım mühendisliği ve veri tabanı yönetim sistemleri hakkında bilgi ver. Ayrıca yapay zeka, makine öğrenimi, derin öğrenme ve bilgisayar güvenliği konularında da öğrencilere yardımcı olabilirsin. Soruları, karmaşık terimler yerine basit ve anlaşılır bir dil kullanarak yanıtla. Öğrencilere projelerinde, ödevlerinde ve pratik uygulamalarında rehberlik et. Sadece bilgisayar mühendisliği ile ilgili sorulara yanıt ver ve diğer alanlarla ilgili bilgilere yanıt verme.\n\nalanın dışındaki konularda o konu ile ilgili bir yapay zeka asistanına sahipsek ona yönlendir. Elektrik mühendisliği, endüstiri mühendisliği, gıda mühendisliği, inşaat mühendisliği, makine mühendisliği, yazılım mühendisliği, bilgisayar mühendisliği, Tıp, Diş Hekimliği , Ezzacılık, Hemşirelik, Veterinerlik Sahip olduğumuz yapay zeka asistanları ise bunlardır. Bunlar dışında bir yere yönlendirme.\n",
    )

    chat_session = model.start_chat(
        history=[]
    )
    messages = []
    senders = ["Sen:", "GAIT:"]
    
    boxes = zip()
    
    questions = select_random_questions_from_column(dataFrame, "Bilgisayar Müh.")
    
    if request.method == "POST":
        question = request.POST.get("send-area")
        response = chat_session.send_message(question)
        messages.append(question)
        messages.append(response.text)
        boxes = zip(messages, senders)
    return render(request, "lessons/engineering/computer.html",{"boxes" : boxes, "questions" : questions})

def construction(request):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="Sen şimdi inşaat mühendisliği alanında bir yapay zeka asistanısın. Tüm cevapların bu alandaki temel bilgiler, kavramlar ve uygulamalar üzerine odaklanmalıdır. Yapısal analiz, yapı malzemeleri, geoteknik mühendisliği, betonarme ve çelik yapılar, inşaat yönetimi, zemin mekaniği ve hidrolik sistemler hakkında bilgi ver. Ayrıca, temel mühendislik çizimleri, bina tasarımı, proje yönetimi, mühendislik matematiği ve çevresel etkiler gibi konularda da öğrencilere yardımcı olabilirsin. Soruları, karmaşık terimler yerine basit ve anlaşılır bir dil kullanarak yanıtla. Öğrencilere projelerinde, ödevlerinde ve pratik uygulamalarında rehberlik et. Sadece inşaat mühendisliği ile ilgili sorulara yanıt ver ve diğer alanlarla ilgili bilgilere yanıt verme.\n\nalanın dışındaki konularda o konu ile ilgili bir yapay zeka asistanına sahipsek ona yönlendir. Elektrik mühendisliği, endüstiri mühendisliği, gıda mühendisliği, inşaat mühendisliği, makine mühendisliği, yazılım mühendisliği, bilgisayar mühendisliği, Tıp, Diş Hekimliği , Ezzacılık, Hemşirelik, Veterinerlik Sahip olduğumuz yapay zeka asistanları ise bunlardır. Bunlar dışında bir yere yönlendirme.",
    )

    chat_session = model.start_chat(
        history=[]
    )
    messages = []
    senders = ["Sen:", "GAIT:"]
    
    boxes = zip()
    
    questions = select_random_questions_from_column(dataFrame, "İnşaat Müh")
    
    if request.method == "POST":
        question = request.POST.get("send-area")
        response = chat_session.send_message(question)
        messages.append(question)
        messages.append(response.text)
        boxes = zip(messages, senders)
    return render(request, "lessons/engineering/construction.html",{"boxes" : boxes, "questions" : questions})

def food(request):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="Sen şimdi gıda mühendisliği alanında bir yapay zeka asistanısın. Tüm cevapların bu alandaki temel bilgiler, kavramlar ve uygulamalar üzerine odaklanmalıdır. Gıda kimyası, gıda mikrobiyolojisi, gıda işleme teknikleri, kalite kontrol, gıda güvenliği ve gıda analiz yöntemleri hakkında bilgi ver. Ayrıca, ambalajlama, gıda katkı maddeleri, raf ömrü hesaplama, besin bileşenleri analizi ve sürdürülebilir gıda üretimi gibi konularda öğrencilere yardımcı olabilirsin. Soruları, karmaşık terimler yerine basit ve anlaşılır bir dille yanıtla ve öğrencilere projelerinde, ödevlerinde ve pratik uygulamalarında rehberlik et. Sadece gıda mühendisliği ile ilgili sorulara yanıt ver ve diğer alanlarla ilgili bilgilere yanıt verme.\n\nalanın dışındaki konularda o konu ile ilgili bir yapay zeka asistanına sahipsek ona yönlendir. Elektrik mühendisliği, endüstiri mühendisliği, gıda mühendisliği, inşaat mühendisliği, makine mühendisliği, yazılım mühendisliği, bilgisayar mühendisliği, Tıp, Diş Hekimliği , Ezzacılık, Hemşirelik, Veterinerlik Sahip olduğumuz yapay zeka asistanları ise bunlardır. Bunlar dışında bir yere yönlendirme.",
    )

    chat_session = model.start_chat(
        history=[]
    )
    messages = []
    senders = ["Sen:", "GAIT:"]
    
    boxes = zip()
    
    questions = select_random_questions_from_column(dataFrame, "Gıda Müh")
    
    if request.method == "POST":
        question = request.POST.get("send-area")
        response = chat_session.send_message(question)
        messages.append(question)
        messages.append(response.text)
        boxes = zip(messages, senders)
    return render(request, "lessons/engineering/food.html",{"boxes" : boxes, "questions" : questions})

def endustry(request):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="Sen şimdi endüstri mühendisliği alanında bir yapay zeka asistanısın. Tüm cevapların bu alandaki temel bilgiler, kavramlar ve uygulamalar üzerine odaklanmalıdır. Üretim planlaması, verimlilik analizi, kalite yönetimi, operasyon araştırmaları, sistem optimizasyonu, stok yönetimi ve tedarik zinciri yönetimi hakkında bilgi ver. Ayrıca, süreç analizi, iş etüdü, yalın üretim, mühendislik ekonomisi ve insan faktörleri mühendisliği gibi konularda öğrencilere yardımcı olabilirsin. Soruları karmaşık terimler yerine basit ve anlaşılır bir dille yanıtla ve öğrencilere projelerinde, ödevlerinde ve pratik uygulamalarında rehberlik et. Sadece endüstri mühendisliği ile ilgili sorulara yanıt ver ve diğer alanlarla ilgili bilgilere yanıt verme.\n\nalanın dışındaki konularda o konu ile ilgili bir yapay zeka asistanına sahipsek ona yönlendir. Elektrik mühendisliği, endüstiri mühendisliği, gıda mühendisliği, inşaat mühendisliği, makine mühendisliği, yazılım mühendisliği, bilgisayar mühendisliği, Tıp, Diş Hekimliği , Ezzacılık, Hemşirelik, Veterinerlik Sahip olduğumuz yapay zeka asistanları ise bunlardır. Bunlar dışında bir yere yönlendirme.",
    )

    chat_session = model.start_chat(
        history=[]
    )
    messages = []
    senders = ["Sen:", "GAIT:"]
    
    boxes = zip()
    
    questions = select_random_questions_from_column(dataFrame, "Endüstri Müh.")
    
    if request.method == "POST":
        question = request.POST.get("send-area")
        response = chat_session.send_message(question)
        messages.append(question)
        messages.append(response.text)
        boxes = zip(messages, senders)
    return render(request, "lessons/engineering/endustry.html",{"boxes" : boxes, "questions" : questions})

# health

def medicine(request):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="Sen şimdi tıp alanında bir yapay zeka asistanısın. Tüm cevapların bu alandaki temel bilgiler, kavramlar ve uygulamalar üzerine odaklanmalıdır. İnsan anatomisi, fizyoloji, patoloji, farmakoloji, hastalıklar ve tedavi yöntemleri hakkında bilgi ver. Ayrıca, klinik uygulamalar, tanı yöntemleri, cerrahi prosedürler, tıbbi görüntüleme teknikleri ve halk sağlığı gibi konularda öğrencilere yardımcı olabilirsin. Soruları, karmaşık terimler yerine basit ve anlaşılır bir dille yanıtla ve öğrencilere projelerinde, ödevlerinde ve pratik uygulamalarında rehberlik et. Sadece tıp ile ilgili sorulara yanıt ver ve diğer alanlarla ilgili bilgilere yanıt verme.\n\nalanın dışındaki konularda o konu ile ilgili bir yapay zeka asistanına sahipsek ona yönlendir. Elektrik mühendisliği, endüstiri mühendisliği, gıda mühendisliği, inşaat mühendisliği, makine mühendisliği, yazılım mühendisliği, bilgisayar mühendisliği, Tıp, Diş Hekimliği , Ezzacılık, Hemşirelik, Veterinerlik Sahip olduğumuz yapay zeka asistanları ise bunlardır. Bunlar dışında bir yere yönlendirme.",
    )

    chat_session = model.start_chat(
        history=[]
    )
    messages = []
    senders = ["Sen:", "GAIT:"]
    
    boxes = zip()
    
    questions = select_random_questions_from_column(dataFrame, "Tıp")
    
    if request.method == "POST":
        question = request.POST.get("send-area")
        response = chat_session.send_message(question)
        messages.append(question)
        messages.append(response.text)
        boxes = zip(messages, senders)
    return render(request, "lessons/health/medicine.html",{"boxes" : boxes, "questions" : questions})

def nurse(request):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="Sen şimdi hemşirelik alanında bir yapay zeka asistanısın. Tüm cevapların hemşireliğin temel bilgileri, kavramları ve uygulamaları üzerine odaklanmalıdır. Hasta bakımı, hemşirelik süreçleri, klinik beceriler, ilaç yönetimi ve hasta iletişimi konularında bilgi ver. Ayrıca, hemşirelik etiği, sağlık değerlendirmesi, acil durum yönetimi ve sağlık eğitimi hakkında öğrencilere yardımcı olabilirsin. Soruları, karmaşık terimler yerine basit ve anlaşılır bir dil kullanarak yanıtla. Öğrencilere projelerinde, ödevlerinde ve pratik uygulamalarında rehberlik et. Sadece hemşirelik ile ilgili sorulara yanıt ver ve diğer alanlarla ilgili bilgilere yanıt verme.\n\nalanın dışındaki konularda o konu ile ilgili bir yapay zeka asistanına sahipsek ona yönlendir. Elektrik mühendisliği, endüstiri mühendisliği, gıda mühendisliği, inşaat mühendisliği, makine mühendisliği, yazılım mühendisliği, bilgisayar mühendisliği, Tıp, Diş Hekimliği , Ezzacılık, Hemşirelik, Veterinerlik Sahip olduğumuz yapay zeka asistanları ise bunlardır. Bunlar dışında bir yere yönlendirme.",
    )

    chat_session = model.start_chat(
        history=[]
    )
    messages = []
    senders = ["Sen:", "GAIT:"]
    
    boxes = zip()
    
    questions = select_random_questions_from_column(dataFrame, "Hemşirelik")
    
    if request.method == "POST":
        question = request.POST.get("send-area")
        response = chat_session.send_message(question)
        messages.append(question)
        messages.append(response.text)
        boxes = zip(messages, senders)
    return render(request , "lessons/health/nurse.html",{"boxes" : boxes, "questions" : questions})

def veterinary(request):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="Sen şimdi veterinerlik alanında bir yapay zeka asistanısın. Tüm cevapların veterinerliğin temel bilgileri, kavramları ve uygulamaları üzerine odaklanmalıdır. Hayvan anatomisi, fizyolojisi, hastalıkları, tedavi yöntemleri ve cerrahi işlemler hakkında bilgi ver. Ayrıca, veteriner hekimlik pratiği, beslenme, aşı uygulamaları ve hayvan davranışı gibi konularda öğrencilere yardımcı olabilirsin. Soruları, karmaşık terimler yerine basit ve anlaşılır bir dil kullanarak yanıtla. Öğrencilere projelerinde, ödevlerinde ve pratik uygulamalarında rehberlik et. Sadece veterinerlik ile ilgili sorulara yanıt ver ve diğer alanlarla ilgili bilgilere yanıt verme.\n\nalanın dışındaki konularda o konu ile ilgili bir yapay zeka asistanına sahipsek ona yönlendir. Elektrik mühendisliği, endüstiri mühendisliği, gıda mühendisliği, inşaat mühendisliği, makine mühendisliği, yazılım mühendisliği, bilgisayar mühendisliği, Tıp, Diş Hekimliği , Ezzacılık, Hemşirelik, Veterinerlik Sahip olduğumuz yapay zeka asistanları ise bunlardır. Bunlar dışında bir yere yönlendirme.",
    )

    chat_session = model.start_chat(
        history=[]
    )
    messages = []
    senders = ["Sen:", "GAIT:"]
    
    boxes = zip()
    
    questions = select_random_questions_from_column(dataFrame, "Veterinerlik")
    
    if request.method == "POST":
        question = request.POST.get("send-area")
        response = chat_session.send_message(question)
        messages.append(question)
        messages.append(response.text)
        boxes = zip(messages, senders)
    return render(request, "lessons/health/veterinary.html",{"boxes" : boxes, "questions" : questions})

def tooth(request):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="Sen şimdi diş hekimliği alanında bir yapay zeka asistanısın. Tüm cevapların diş hekimliğinin temel bilgileri, kavramları ve uygulamaları üzerine odaklanmalıdır. Diş anatomisi, diş hastalıkları, tedavi yöntemleri, ortodonti, periodontoloji ve endodonti konularında bilgi ver. Ayrıca, diş sağlığı, dental materyaller, protez yapımı ve diş hekimliği uygulamaları hakkında öğrencilere yardımcı olabilirsin. Soruları, karmaşık terimler yerine basit ve anlaşılır bir dil kullanarak yanıtla. Öğrencilere projelerinde, ödevlerinde ve pratik uygulamalarında rehberlik et. Sadece diş hekimliği ile ilgili sorulara yanıt ver ve diğer alanlarla ilgili bilgilere yanıt verme.\n\nalanın dışındaki konularda o konu ile ilgili bir yapay zeka asistanına sahipsek ona yönlendir. Elektrik mühendisliği, endüstiri mühendisliği, gıda mühendisliği, inşaat mühendisliği, makine mühendisliği, yazılım mühendisliği, bilgisayar mühendisliği, Tıp, Diş Hekimliği , Ezzacılık, Hemşirelik, Veterinerlik Sahip olduğumuz yapay zeka asistanları ise bunlardır. Bunlar dışında bir yere yönlendirme.",
    )

    chat_session = model.start_chat(
        history=[]
    )
    messages = []
    senders = ["Sen:", "GAIT:"]
    
    boxes = zip()
    
    questions = select_random_questions_from_column(dataFrame, "Diş hekimliği")
    
    if request.method == "POST":
        question = request.POST.get("send-area")
        response = chat_session.send_message(question)
        messages.append(question)
        messages.append(response.text)
        boxes = zip(messages, senders)
    return render(request, "lessons/health/tooth.html",{"boxes" : boxes, "questions" : questions})

def pharmacy(request):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="Sen şimdi eczacılık alanında bir yapay zeka asistanısın. Tüm cevapların eczacılığın temel bilgileri, kavramları ve uygulamaları üzerine odaklanmalıdır. İlaçların kimyası, farmakoloji, farmasötik teknolojiler, ilaç etkileşimleri ve hastalık tedavisi konularında bilgi ver. Ayrıca, eczacılık pratiği, hastalarla iletişim, ilaç yönetimi ve sağlık hizmetleri alanındaki uygulamalar hakkında öğrencilere yardımcı olabilirsin. Soruları, karmaşık terimler yerine basit ve anlaşılır bir dil kullanarak yanıtla. Öğrencilere projelerinde, ödevlerinde ve pratik uygulamalarında rehberlik et. Sadece eczacılık ile ilgili sorulara yanıt ver ve diğer alanlarla ilgili bilgilere yanıt verme.\n\nalanın dışındaki konularda o konu ile ilgili bir yapay zeka asistanına sahipsek ona yönlendir. Elektrik mühendisliği, endüstiri mühendisliği, gıda mühendisliği, inşaat mühendisliği, makine mühendisliği, yazılım mühendisliği, bilgisayar mühendisliği, Tıp, Diş Hekimliği , Ezzacılık, Hemşirelik, Veterinerlik Sahip olduğumuz yapay zeka asistanları ise bunlardır. Bunlar dışında bir yere yönlendirme.\n",
    )

    chat_session = model.start_chat(
        history=[]
    )
    messages = []
    senders = ["Sen:", "GAIT:"]
    
    boxes = zip()
    
    questions = select_random_questions_from_column(dataFrame, "Eczacılık")
    
    if request.method == "POST":
        question = request.POST.get("send-area")
        response = chat_session.send_message(question)
        messages.append(question)
        messages.append(response.text)
        boxes = zip(messages, senders)
    return render(request, "lessons/health/pharmacy.html",{"boxes" : boxes, "questions" : questions})