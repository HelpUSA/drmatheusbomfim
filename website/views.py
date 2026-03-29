# File: website/views.py
# Purpose:
# View functions for the public website.
from django.shortcuts import render


def home(request):
    hero_slides = [
        'website/mid/hero-bg-1.jpg',
        'website/mid/hero-bg-2.jpg',
        'website/mid/hero-bg-3.jpg',
        'website/mid/hero-bg-4.jpg',
    ]

    services = [
        {
            'title': 'Facetas em resina',
            'description': 'Planejamento estético personalizado para transformar o sorriso com naturalidade, equilíbrio e funcionalidade.',
        },
        {
            'title': 'Clareamento dental',
            'description': 'Protocolos pensados para valorizar a harmonia do sorriso e potencializar os resultados estéticos.',
        },
        {
            'title': 'Reabilitação estética e funcional',
            'description': 'Abordagem que une estética, mordida, conforto e previsibilidade no tratamento.',
        },
        {
            'title': 'Lentes de contato dental',
            'description': 'Indicação criteriosa para quem deseja refinamento estético com aparência leve e sofisticada.',
        },
    ]

    differentiators = [
        'Atendimento humanizado e individualizado',
        'Planejamento do sorriso com foco natural',
        'Ambiente moderno e experiência premium',
        'Integração entre estética e função mastigatória',
    ]

    steps = [
        'Avaliação clínica e escuta do seu objetivo',
        'Planejamento do sorriso e definição da proposta',
        'Execução do tratamento com previsibilidade',
        'Acompanhamento e orientações de manutenção',
    ]

    faqs = [
        {
            'question': 'Para quem as facetas em resina são indicadas?',
            'answer': 'São uma excelente alternativa para correções de formato, pequenas fraturas, espaços entre os dentes, manchas e harmonização do sorriso, sempre após avaliação individual.',
        },
        {
            'question': 'O resultado pode ficar natural?',
            'answer': 'Sim. O grande diferencial está no planejamento, escolha de cor, anatomia e proporção do sorriso para que o resultado fique sofisticado e compatível com o rosto do paciente.',
        },
        {
            'question': 'Como agendar uma avaliação?',
            'answer': 'O site já direciona diretamente para o WhatsApp do consultório, facilitando o primeiro contato e o agendamento.',
        },
    ]

    context = {
        'hero_slides': hero_slides,
        'services': services,
        'differentiators': differentiators,
        'steps': steps,
        'faqs': faqs,
        'whatsapp_href': 'https://wa.me/558393062224?text=Olá%2C+quero+agendar+uma+avaliação+com+o+Dr.+Matheus+Bomfim.',
        'instagram_href': 'https://www.instagram.com/dr.matheus_bomfim/',
        'helpus_href': 'https://helpusbr.com',
    }
    return render(request, 'website/index.html', context)
