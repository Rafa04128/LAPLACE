#include <iostream>
#include <vector>
#include <thread>
#include <future>
#include <podofo/podofo.h>

std::string extractTextFromPDF(const std::string& pdfFilePath) {
    std::string text;
    try {
        PoDoFo::PdfMemDocument pdfDocument(pdfFilePath.c_str());
        for (int pageNum = 0; pageNum < pdfDocument.GetPages(); ++pageNum) {
            PoDoFo::PdfRefCountedBuffer buffer;
            PoDoFo::PdfSimpleWriter writer(&buffer);
            pdfDocument.WriteCurrentPage(&writer, pageNum);
            std::string pageText = buffer.GetBuffer();
            text += pageText;
        }
    } catch (const PoDoFo::PdfError& e) {
        std::cerr << "Error reading PDF file " << pdfFilePath << ": " << e.what() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Unexpected error reading " << pdfFilePath << ": " << e.what() << std::endl;
    }
    return text;
}

void saveTextToFile(const std::string& text, const std::string& outputFilePath) {
    try {
        std::ofstream outputFile(outputFilePath, std::ios::out | std::ios::trunc);
        outputFile << text;
        std::cout << "Text saved to " << outputFilePath << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error saving text to file: " << e.what() << std::endl;
    }
}

int main() {
    std::string directoryPath = "C:\\Users\\rafa0\\Desktop\\pj\\laplace\\LAPLACE\\data\\books";
    std::string outputFilePath = "output.txt";

    std::vector<std::future<std::string>> futures;
    for (const auto& entry : std::filesystem::directory_iterator(directoryPath)) {
        if (entry.path().extension() == ".pdf") {
            futures.emplace_back(std::async(std::launch::async, extractTextFromPDF, entry.path().string()));
        }
    }

    std::string textData;
    for (auto&& future : futures) {
        textData += future.get();
    }

    saveTextToFile(textData, outputFilePath);

    return 0;
}