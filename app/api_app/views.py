from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
import requests

class LineView(APIView):
    NUM_DATA = 500

    def get(self, request, *args, **kwargs):
        """
        ランダムに生成されたデータを含むJSONレスポンスを生成して返します。

        パラメータ:
        - request: HTTPリクエスト

        戻り値:
        - Response: 生成されたデータを含むHTTPレスポンス
        """
        query = request.GET

        result_data = []
        if 'projectid' in query:

            projectId = query['projectid']

            if projectId != "123":
                result_data.append({"message": "認証に失敗しました。"})
                return Response(result_data, status=status.HTTP_403_FORBIDDEN)
        else:
                result_data.append({"message": "パラメータが不正です"})
                return Response(result_data, status=status.HTTP_400_BAD_REQUEST)


        # データを生成してリストに追加
        for i in range(1, self.NUM_DATA + 1):
            key = f"データ{i}"
            value = random.randint(1, 100)
            result_data.append({key: value})

        return Response(result_data, status=status.HTTP_200_OK)


class AnimeView(APIView):
 
    def get(self, request, *args, **kwargs):
        """
        メディア芸術データベースJSONレスポンスを返します。

        パラメータ:
        - request: HTTPリクエスト

        戻り値:
        - Response: 生成されたデータを含むHTTPレスポンス
        """

        url = 'https://mediaarts-db.bunka.go.jp/api/search'
        query = {
            'fieldId': 'animation',
            'subcategoryId': 'an207',
            'name': 'コードギアス',
        }
        
        result_data = requests.get(url, params=query)
        
        if result_data.status_code == 200:
            # JSON データに変換して返す
            return Response(result_data.json(), status=status.HTTP_200_OK)
        else:
            # エラーが発生した場合はエラーレスポンスを返す
            return Response(result_data.text, status=result_data.status_code)
