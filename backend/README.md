## Генерация заглушке для сервера
1. Скачать сам генератор по [инструкции](https://github.com/OpenAPITools/openapi-generator?tab=readme-ov-file#13---download-jar)
2. Убедиться, что на машине установлена JRE 11 и выше. При отсутствии скачать можно [отсюда](https://adoptium.net/temurin/releases/?package=jre)
3. Запустить скачанный генератор командой
`java -jar <путь до openapi-generator-cli.jar> generate  -i <путь до openAPI спеки>  -g python-fastapi -o <путь для сгенерированных файлов> --additional-properties=packageName= --additional-properties=fastapiImplementationPackage=endpoints`
4. В файле `<путь до сгенерированных файлов>\src\endpoints\apis\default_api_base.py` можно найти базовый класс с сигнатурами методов, которые необходимо релазиовать, отнаследовавшись от базового класса. Реализацию можно предоставлять в новых файлах по пути <...>\src\endpoints\<ваше название>.py
