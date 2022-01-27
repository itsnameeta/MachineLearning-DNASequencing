import streamlit as st
from Bio import SeqIO
import neatbio.sequtils as utils
from collections import Counter
from Bio.Seq import Seq
import io
import matplotlib.pyplot as plt
import matplotlib
st.set_option('deprecation.showPyplotGlobalUse', False)
import numpy as np


def main():

    st.title("iGENOMICS")
    options = ["Introduction", "DNA sequence Analysis"]
    choices = st.sidebar.selectbox("Choose Your Options",options)

    if choices == "Introduction":
        st.header("Welcome to our DNA Sequence Analysis! ")

    elif choices == "DNA sequence Analysis":
        st.header("For DNA sequence Analysis:")
        seq=st.file_uploader("Upload .FASTA file for Genome DNA analysis", type = ["fasta","fa"])

        if seq is not None:
            data =seq.read()
            decdata = data.decode('UTF-8')
            dnarecord= SeqIO.read(io.StringIO(decdata),"fasta")
            dnaseq= dnarecord.seq

            details= st.radio ("Details of the DNA by NCBI",("DNA Description", "Sequence"))
            if details == "DNA Description":
                st.write(dnarecord.description)
            elif details == "Sequence":
                st.write (dnarecord.seq)

            #Nucleotide
            st.subheader ("Nucleotide Frequency :")
            dnafreq=Counter(dnaseq)
            st.write(dnafreq)
            adenine=st.color_picker("Adenine Colour ")
            guanine=st.color_picker("Guanine Colour ")
            thymine=st.color_picker("Thymine Colour ")
            cytosine=st.color_picker("Cytosine Colour ")


            if st.button("Plot frequency"):
                bar=plt.bar(dnafreq.keys(),dnafreq.values())
                bar[0].set_color(adenine)
                bar[1].set_color(guanine)
                bar[2].set_color(thymine)
                bar[3].set_color(cytosine)
                fig, ax = plt.subplots()
                st.pyplot()


            st.subheader("DNA Composition is as below:")

            gc= utils.gc_content(str(dnaseq))
            at= utils.at_content(str(dnaseq))
            st.json({"GC Content(for heat stability)": gc,"AT Content":at })

            #Protein synthesis
            st.subheader("Protein Synthesis:")
            ps = dnaseq.translate()
            aafreq= Counter(str(ps))
            if st.checkbox("Transcription:"):
                st.write(dna_seq.transcribe())
            elif st.checkbox("Translation:"):
                st.write(dna_seq.translate())
            elif st.checkbox("Complement:"):
                st.write(dna_seq.complement())
            elif st.checkbox("Amino Acid frequency :"):
                st.write(aa_freq)

            elif st.checkbox("Plot the Amino Acid frequency:"):
                aacolor=st.color_picker("Pick the Amino acid color:")
                plt.bar(aafreq.keys(),aa_freq.values(),color=aacolor)
                st.pyplot()

            elif st.checkbox("The complete Amino acid name is given as"):
                aaname= str(ps).replace("*","")
                aa3= utils.convert_1to3(aaname)
                st.write(aaname)
                st.write("========================")
                st.write(aa3)



                st.write("========================")
                st.write(utils.get_acid_name(aa3))

if __name__=='__main__':
	main()