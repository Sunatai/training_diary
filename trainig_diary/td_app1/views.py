from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from plotly.offline import plot
import plotly.express as px
from .models import TrainingDiaryModel
from django.urls import reverse_lazy
import plotly.figure_factory as ff
import pandas as pd
pd.options.plotting.backend = "plotly"
import plotly.io as pio

# Create your views here.
class DiaryList(ListView):
    template_name = 'list.html'
    model = TrainingDiaryModel #どのモデルを使用するかの指定

class DiaryDetail(DetailView):
    template_name = 'detail.html'
    model = TrainingDiaryModel #どのモデルを使用するかの指定

class DiaryCreate(CreateView):
    template_name = 'create.html'
    model = TrainingDiaryModel
    fields = ('body_part','train_name','weight','raise_times','set_times','date','memo')
    success_url = reverse_lazy('list')

class DiaryDelete(DeleteView):
    template_name = 'delete.html'
    model = TrainingDiaryModel
    success_url = reverse_lazy('list')

class DiaryUpdate(UpdateView):
    template_name = 'update.html'
    model = TrainingDiaryModel
    fields = ('body_part','train_name','weight','raise_times','set_times','date','memo')
    success_url = reverse_lazy('list')

class DiaryTest(ListView):
    template_name = 'test.html'
    model = TrainingDiaryModel

import plotly.offline as opy
import plotly.graph_objs as go

def hello_template(request):

    result_chest = TrainingDiaryModel.objects.filter(body_part='warning')
    result_leg = TrainingDiaryModel.objects.filter(body_part='success')
    result_back = TrainingDiaryModel.objects.filter(body_part='primary')
    result = TrainingDiaryModel.objects.all()

    pon=[]
    pon_t=[]
    for line in result:
        pon.append(line.weight)
        pon.append(line.raise_times)
        pon.append(line.set_times)
        pon.append(line.date)
        pon.append(line.weight * line.set_times * line.raise_times)
        pon.append(line.body_part)
        pon_t.append(pon)
        pon=[]
    box=[]

    data_chest = []
    data_chest_date = []
    data_chest_total=[]
    for chest in result_chest:
        box.clear()
        box.append(chest.weight)
        box.append(chest.raise_times)
        box.append(chest.set_times)
        box.append(chest.date)
        box.append(chest.weight*chest.set_times*chest.raise_times)
        data_chest.append(box)

    #_hest_weight=[a for a in data_chest[a][0]]

    data_back = []
    data_back_date=[]
    data_back_total=[]
    for back in result_back:
        box.clear()
        box.append(back.weight)
        box.append(back.raise_times)
        box.append(back.set_times)
        data_back_date.append(back.date)
        data_back_total.append(back.weight*back.set_times*back.raise_times)
        data_back.append(box)

    data_leg = []
    data_leg_date=[]
    data_leg_total=[]
    for leg in result_leg:
        box.clear()
        box.append(leg.weight)
        box.append(leg.raise_times)
        box.append(leg.set_times)
        box.append(leg.weight * leg.set_times * leg.raise_times)
        data_leg.append(box)
        box.append(leg.date)

#1.重さ、2.回数,3.セット数,4.トータル重量

    # for data in result:
    #     data_weight.append(data.weight)
    #     data_date.append(data.date)
    #     data_raise_times.append(data.raise_times)
    #     data_set_times.append(data.set_times)

    df = pd.DataFrame(pon_t,columns=['重さ','回数','セット数','日付','トータル重量','部位'])
    trace = go.Figure(data=go.Bar(x=data_back_date, y=data_back_total))
    trace1= go.Figure(data=go.Bar(x=data_leg_date, y=data_leg_total))
    #fig2= go.Figure(data=go.Bar(x=[data_back_date], y=data_back_total))
    #fig = [go.Bar(x=df['日付'],y=df.iloc[:, i])for i in range(0,2)]
    #fig = df.plot()

    # trace1 = go.Histogram(
    #     x=data_back_date,
    #     name="data1",
    #     marker=dict(color='#FFD7E9'),
    #     opacity=0.75
    # )
    # trace2 = go.Histogram(
    #     x=data_leg_date,
    #     name="data2",
    #     marker=dict(color='#EB89B5'),
    #     opacity=0.75
    # )
    #
    # layout = go.Layout(
    #     title="two histograms",
    #     xaxis=dict(title="value"),
    #     yaxis=dict(title="Count"),
    #     bargap=0.2,  # barの間隔を指定します
    #     bargroupgap=0.1
    # )

    fig = px.bar(df, x="日付", y="トータル重量", color="部位", title="Long-Form Input")
    # fig.update_layout(
    #     title_text='トレーニンググラフ',
    #     xaxis_title_text='日付',
    #     yaxis_title_text='トータル重量(kg)',
    #     bargap=0.2,  # 隣接する位置座標のバー間のギャップ
    #     bargroupgap=0.1,
    # )
    plot_html = plot(fig, output_type='div', include_plotlyjs=False)
    d = {
        'message': plot_html,
    }
    return render(request, 'index.html', d)

result = TrainingDiaryModel.objects.all()
pon=[]
pon_t=[]
for line in result:
    pon.append(line.weight)
    pon.append(line.raise_times)
    pon.append(line.set_times)
    pon.append(line.date)
    pon.append(line.weight * line.set_times * line.raise_times)
    pon.append(line.body_part)
    pon_t.append(pon)
    pon=[]
print(pon_t)
df = pd.DataFrame(pon_t,columns=['重さ','回数','セット数','日付','トータル重量','部位'])
print(df)

# result_leg = TrainingDiaryModel.objects.filter(body_part='success')
# data_leg=[]
# box=[]
# for leg in result_leg:
#     box.clear()
#     box.append(leg.weight)
#     box.append(leg.raise_times)
#     box.append(leg.set_times)
#     box.append(leg.date)
#     box.append(leg.weight * leg.set_times * leg.raise_times)
#     data_leg.append(box)
#
# print(data_leg)
# df = pd.DataFrame(data_leg,columns=['重さ','回数','セット数','日付','総重量'])
# #fig = go.Figure(data=go.Bar(x=, y=df.index, name='胸'))
# print(df)



