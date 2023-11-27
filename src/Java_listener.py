# Generated from Java8.g4 by ANTLR 4.13.1
from antlr4 import *
from Java8Listener import Java8Listener
from Java8Parser import Java8Parser


# This class defines a complete listener for a parse tree produced by Java8Parser.
class Java8Listener(ParseTreeListener):

    def __init__(self):
        self.foundInMethodBody = set()
        self.Cyclomatic = 0

    # Enter a parse tree produced by Java8Parser#literal.
    def enterLiteral(self, ctx:Java8Parser.LiteralContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#type.
    def enterType(self, ctx:Java8Parser.TypeContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

        # Enter a parse tree produced by Java8Parser#primitiveType.
    def enterPrimitiveType(self, ctx:Java8Parser.PrimitiveTypeContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#classOrInterfaceType.
    def enterClassOrInterfaceType(self, ctx:Java8Parser.ClassOrInterfaceTypeContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#classType.
    def enterClassType(self, ctx:Java8Parser.ClassTypeContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#interfaceType.
    def enterInterfaceType(self, ctx:Java8Parser.InterfaceTypeContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#typeVariable.
    def enterTypeVariable(self, ctx:Java8Parser.TypeVariableContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#arrayType.
    def enterArrayType(self, ctx:Java8Parser.ArrayTypeContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#dims.
    def enterDims(self, ctx:Java8Parser.DimsContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#typeParameter.
    def enterTypeParameter(self, ctx:Java8Parser.TypeParameterContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#typeBound.
    def enterTypeBound(self, ctx:Java8Parser.TypeBoundContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#additionalBound.
    def enterAdditionalBound(self, ctx:Java8Parser.AdditionalBoundContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#typeArguments.
    def enterTypeArguments(self, ctx:Java8Parser.TypeArgumentsContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#typeArgumentList.
    def enterTypeArgumentList(self, ctx:Java8Parser.TypeArgumentListContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#typeArgument.
    def enterTypeArgument(self, ctx:Java8Parser.TypeArgumentContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#wildcard.
    def enterWildcard(self, ctx:Java8Parser.WildcardContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#wildcardBounds.
    def enterWildcardBounds(self, ctx:Java8Parser.WildcardBoundsContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#packageName.
    def enterPackageName(self, ctx:Java8Parser.PackageNameContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#typeName.
    def enterTypeName(self, ctx:Java8Parser.TypeNameContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#packageOrTypeName.
    def enterPackageOrTypeName(self, ctx:Java8Parser.PackageOrTypeNameContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#expressionName.
    def enterExpressionName(self, ctx:Java8Parser.ExpressionNameContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#methodName.
    def enterMethodName(self, ctx:Java8Parser.MethodNameContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#ambiguousName.
    def enterAmbiguousName(self, ctx:Java8Parser.AmbiguousNameContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#compilationUnit.
    def enterCompilationUnit(self, ctx:Java8Parser.CompilationUnitContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#packageDeclaration.
    def enterPackageDeclaration(self, ctx:Java8Parser.PackageDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#importDeclaration.
    def enterImportDeclaration(self, ctx:Java8Parser.ImportDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#singleTypeImportDeclaration.
    def enterSingleTypeImportDeclaration(self, ctx:Java8Parser.SingleTypeImportDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#typeImportOnDemandDeclaration.
    def enterTypeImportOnDemandDeclaration(self, ctx:Java8Parser.TypeImportOnDemandDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#singleStaticImportDeclaration.
    def enterSingleStaticImportDeclaration(self, ctx:Java8Parser.SingleStaticImportDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#staticImportOnDemandDeclaration.
    def enterStaticImportOnDemandDeclaration(self, ctx:Java8Parser.StaticImportOnDemandDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:Java8Parser.TypeDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#classDeclaration.
    def enterClassDeclaration(self, ctx:Java8Parser.ClassDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#normalClassDeclaration.
    def enterNormalClassDeclaration(self, ctx:Java8Parser.NormalClassDeclarationContext):
        self.className = ctx.Identifier()
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    def get_class(self):
        return self.className
    
    # Enter a parse tree produced by Java8Parser#typeParameters.
    def enterTypeParameters(self, ctx:Java8Parser.TypeParametersContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#typeParameterList.
    def enterTypeParameterList(self, ctx:Java8Parser.TypeParameterListContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#superclass.
    def enterSuperclass(self, ctx:Java8Parser.SuperclassContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#superinterfaces.
    def enterSuperinterfaces(self, ctx:Java8Parser.SuperinterfacesContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#interfaceTypeList.
    def enterInterfaceTypeList(self, ctx:Java8Parser.InterfaceTypeListContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#classBody.
    def enterClassBody(self, ctx:Java8Parser.ClassBodyContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#classBodyDeclaration.
    def enterClassBodyDeclaration(self, ctx:Java8Parser.ClassBodyDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#classMemberDeclaration.
    def enterClassMemberDeclaration(self, ctx:Java8Parser.ClassMemberDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:Java8Parser.FieldDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#variableDeclaratorList.
    def enterVariableDeclaratorList(self, ctx:Java8Parser.VariableDeclaratorListContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:Java8Parser.VariableDeclaratorContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#variableDeclaratorId.
    def enterVariableDeclaratorId(self, ctx:Java8Parser.VariableDeclaratorIdContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#variableInitializer.
    def enterVariableInitializer(self, ctx:Java8Parser.VariableInitializerContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#unannType.
    def enterUnannType(self, ctx:Java8Parser.UnannTypeContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#unannPrimitiveType.
    def enterUnannPrimitiveType(self, ctx:Java8Parser.UnannPrimitiveTypeContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#unannReferenceType.
    def enterUnannReferenceType(self, ctx:Java8Parser.UnannReferenceTypeContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#unannClassOrInterfaceType.
    def enterUnannClassOrInterfaceType(self, ctx:Java8Parser.UnannClassOrInterfaceTypeContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#unannClassType.
    def enterUnannClassType(self, ctx:Java8Parser.UnannClassTypeContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#unannInterfaceType.
    def enterUnannInterfaceType(self, ctx:Java8Parser.UnannInterfaceTypeContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#unannTypeVariable.
    def enterUnannTypeVariable(self, ctx:Java8Parser.UnannTypeVariableContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#unannArrayType.
    def enterUnannArrayType(self, ctx:Java8Parser.UnannArrayTypeContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:Java8Parser.MethodDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#methodHeader.
    def enterMethodHeader(self, ctx:Java8Parser.MethodHeaderContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#result.
    def enterResult(self, ctx:Java8Parser.ResultContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#methodDeclarator.
    def enterMethodDeclarator(self, ctx:Java8Parser.MethodDeclaratorContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#formalParameterList.
    def enterFormalParameterList(self, ctx:Java8Parser.FormalParameterListContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#formalParameters.
    def enterFormalParameters(self, ctx:Java8Parser.FormalParametersContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#formalParameter.
    def enterFormalParameter(self, ctx:Java8Parser.FormalParameterContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#variableModifier.
    def enterVariableModifier(self, ctx:Java8Parser.VariableModifierContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#lastFormalParameter.
    def enterLastFormalParameter(self, ctx:Java8Parser.LastFormalParameterContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#receiverParameter.
    def enterReceiverParameter(self, ctx:Java8Parser.ReceiverParameterContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#throws_.
    def enterThrows_(self, ctx:Java8Parser.Throws_Context):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#exceptionTypeList.
    def enterExceptionTypeList(self, ctx:Java8Parser.ExceptionTypeListContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#exceptionType.
    def enterExceptionType(self, ctx:Java8Parser.ExceptionTypeContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#methodBody.
    def enterMethodBody(self, ctx:Java8Parser.MethodBodyContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#instanceInitializer.
    def enterInstanceInitializer(self, ctx:Java8Parser.InstanceInitializerContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#staticInitializer.
    def enterStaticInitializer(self, ctx:Java8Parser.StaticInitializerContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:Java8Parser.ConstructorDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#constructorDeclarator.
    def enterConstructorDeclarator(self, ctx:Java8Parser.ConstructorDeclaratorContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#simpleTypeName.
    def enterSimpleTypeName(self, ctx:Java8Parser.SimpleTypeNameContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#constructorBody.
    def enterConstructorBody(self, ctx:Java8Parser.ConstructorBodyContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#explicitConstructorInvocation.
    def enterExplicitConstructorInvocation(self, ctx:Java8Parser.ExplicitConstructorInvocationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:Java8Parser.EnumDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#enumBody.
    def enterEnumBody(self, ctx:Java8Parser.EnumBodyContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#enumConstantList.
    def enterEnumConstantList(self, ctx:Java8Parser.EnumConstantListContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#enumConstant.
    def enterEnumConstant(self, ctx:Java8Parser.EnumConstantContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#enumBodyDeclarations.
    def enterEnumBodyDeclarations(self, ctx:Java8Parser.EnumBodyDeclarationsContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:Java8Parser.InterfaceDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#normalInterfaceDeclaration.
    def enterNormalInterfaceDeclaration(self, ctx:Java8Parser.NormalInterfaceDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#extendsInterfaces.
    def enterExtendsInterfaces(self, ctx:Java8Parser.ExtendsInterfacesContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#interfaceBody.
    def enterInterfaceBody(self, ctx:Java8Parser.InterfaceBodyContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#interfaceMemberDeclaration.
    def enterInterfaceMemberDeclaration(self, ctx:Java8Parser.InterfaceMemberDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#constantDeclaration.
    def enterConstantDeclaration(self, ctx:Java8Parser.ConstantDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#interfaceMethodDeclaration.
    def enterInterfaceMethodDeclaration(self, ctx:Java8Parser.InterfaceMethodDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#annotationTypeDeclaration.
    def enterAnnotationTypeDeclaration(self, ctx:Java8Parser.AnnotationTypeDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#annotationTypeBody.
    def enterAnnotationTypeBody(self, ctx:Java8Parser.AnnotationTypeBodyContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#annotationTypeMemberDeclaration.
    def enterAnnotationTypeMemberDeclaration(self, ctx:Java8Parser.AnnotationTypeMemberDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#annotationTypeElementDeclaration.
    def enterAnnotationTypeElementDeclaration(self, ctx:Java8Parser.AnnotationTypeElementDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#defaultValue.
    def enterDefaultValue(self, ctx:Java8Parser.DefaultValueContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#annotation.
    def enterAnnotation(self, ctx:Java8Parser.AnnotationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#normalAnnotation.
    def enterNormalAnnotation(self, ctx:Java8Parser.NormalAnnotationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#elementValuePairList.
    def enterElementValuePairList(self, ctx:Java8Parser.ElementValuePairListContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#elementValuePair.
    def enterElementValuePair(self, ctx:Java8Parser.ElementValuePairContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#elementValue.
    def enterElementValue(self, ctx:Java8Parser.ElementValueContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#elementValueArrayInitializer.
    def enterElementValueArrayInitializer(self, ctx:Java8Parser.ElementValueArrayInitializerContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#elementValueList.
    def enterElementValueList(self, ctx:Java8Parser.ElementValueListContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#markerAnnotation.
    def enterMarkerAnnotation(self, ctx:Java8Parser.MarkerAnnotationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#singleElementAnnotation.
    def enterSingleElementAnnotation(self, ctx:Java8Parser.SingleElementAnnotationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#arrayInitializer.
    def enterArrayInitializer(self, ctx:Java8Parser.ArrayInitializerContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#variableInitializerList.
    def enterVariableInitializerList(self, ctx:Java8Parser.VariableInitializerListContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#block.
    def enterBlock(self, ctx:Java8Parser.BlockContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#blockStatements.
    def enterBlockStatements(self, ctx:Java8Parser.BlockStatementsContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#blockStatement.
    def enterBlockStatement(self, ctx:Java8Parser.BlockStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])
        
    # Enter a parse tree produced by Java8Parser#localVariableDeclarationStatement.
    def enterLocalVariableDeclarationStatement(self, ctx:Java8Parser.LocalVariableDeclarationStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:Java8Parser.LocalVariableDeclarationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#statement.
    def enterStatement(self, ctx:Java8Parser.StatementContext):
        statement_text = ctx.getText()
        if "System.out.print" in statement_text:
            self.foundInMethodBody.add("print")

        if "\\t" in statement_text or "\\n" in statement_text:
            self.foundInMethodBody.add("escape")

        if "Math.random" in statement_text or "Math.sqrt" in statement_text or "Math.pow" in statement_text:
            self.foundInMethodBody.add("math")
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#statementNoShortIf.
    def enterStatementNoShortIf(self, ctx:Java8Parser.StatementNoShortIfContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#statementWithoutTrailingSubstatement.
    def enterStatementWithoutTrailingSubstatement(self, ctx:Java8Parser.StatementWithoutTrailingSubstatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#emptyStatement.
    def enterEmptyStatement(self, ctx:Java8Parser.EmptyStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#labeledStatement.
    def enterLabeledStatement(self, ctx:Java8Parser.LabeledStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#labeledStatementNoShortIf.
    def enterLabeledStatementNoShortIf(self, ctx:Java8Parser.LabeledStatementNoShortIfContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#expressionStatement.
    def enterExpressionStatement(self, ctx:Java8Parser.ExpressionStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#statementExpression.
    def enterStatementExpression(self, ctx:Java8Parser.StatementExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#ifThenStatement.
    def enterIfThenStatement(self, ctx:Java8Parser.IfThenStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])
        self.Cyclomatic += 1

    # Enter a parse tree produced by Java8Parser#ifThenElseStatement.
    def enterIfThenElseStatement(self, ctx:Java8Parser.IfThenElseStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])
        self.Cyclomatic += 1

    # Enter a parse tree produced by Java8Parser#ifThenElseStatementNoShortIf.
    def enterIfThenElseStatementNoShortIf(self, ctx:Java8Parser.IfThenElseStatementNoShortIfContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])
        self.Cyclomatic += 1

    # Enter a parse tree produced by Java8Parser#assertStatement.
    def enterAssertStatement(self, ctx:Java8Parser.AssertStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#switchStatement.
    def enterSwitchStatement(self, ctx:Java8Parser.SwitchStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#switchBlock.
    def enterSwitchBlock(self, ctx:Java8Parser.SwitchBlockContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#switchBlockStatementGroup.
    def enterSwitchBlockStatementGroup(self, ctx:Java8Parser.SwitchBlockStatementGroupContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#switchLabels.
    def enterSwitchLabels(self, ctx:Java8Parser.SwitchLabelsContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#switchLabel.
    def enterSwitchLabel(self, ctx:Java8Parser.SwitchLabelContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#enumConstantName.
    def enterEnumConstantName(self, ctx:Java8Parser.EnumConstantNameContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#whileStatement.
    def enterWhileStatement(self, ctx:Java8Parser.WhileStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#whileStatementNoShortIf.
    def enterWhileStatementNoShortIf(self, ctx:Java8Parser.WhileStatementNoShortIfContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#doStatement.
    def enterDoStatement(self, ctx:Java8Parser.DoStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#forStatement.
    def enterForStatement(self, ctx:Java8Parser.ForStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])
        self.Cyclomatic += 1

    # Enter a parse tree produced by Java8Parser#forStatementNoShortIf.
    def enterForStatementNoShortIf(self, ctx:Java8Parser.ForStatementNoShortIfContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#basicForStatement.
    def enterBasicForStatement(self, ctx:Java8Parser.BasicForStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])
        # self.Cyclomatic += 1

    # Enter a parse tree produced by Java8Parser#basicForStatementNoShortIf.
    def enterBasicForStatementNoShortIf(self, ctx:Java8Parser.BasicForStatementNoShortIfContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])
        
    # Enter a parse tree produced by Java8Parser#forInit.
    def enterForInit(self, ctx:Java8Parser.ForInitContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#forUpdate.
    def enterForUpdate(self, ctx:Java8Parser.ForUpdateContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#statementExpressionList.
    def enterStatementExpressionList(self, ctx:Java8Parser.StatementExpressionListContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#enhancedForStatement.
    def enterEnhancedForStatement(self, ctx:Java8Parser.EnhancedForStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#enhancedForStatementNoShortIf.
    def enterEnhancedForStatementNoShortIf(self, ctx:Java8Parser.EnhancedForStatementNoShortIfContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#breakStatement.
    def enterBreakStatement(self, ctx:Java8Parser.BreakStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#continueStatement.
    def enterContinueStatement(self, ctx:Java8Parser.ContinueStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#returnStatement.
    def enterReturnStatement(self, ctx:Java8Parser.ReturnStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#throwStatement.
    def enterThrowStatement(self, ctx:Java8Parser.ThrowStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#synchronizedStatement.
    def enterSynchronizedStatement(self, ctx:Java8Parser.SynchronizedStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#tryStatement.
    def enterTryStatement(self, ctx:Java8Parser.TryStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#catches.
    def enterCatches(self, ctx:Java8Parser.CatchesContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#catchClause.
    def enterCatchClause(self, ctx:Java8Parser.CatchClauseContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#catchFormalParameter.
    def enterCatchFormalParameter(self, ctx:Java8Parser.CatchFormalParameterContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#catchType.
    def enterCatchType(self, ctx:Java8Parser.CatchTypeContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#finally_.
    def enterFinally_(self, ctx:Java8Parser.Finally_Context):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#tryWithResourcesStatement.
    def enterTryWithResourcesStatement(self, ctx:Java8Parser.TryWithResourcesStatementContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#resourceSpecification.
    def enterResourceSpecification(self, ctx:Java8Parser.ResourceSpecificationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#resourceList.
    def enterResourceList(self, ctx:Java8Parser.ResourceListContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#resource.
    def enterResource(self, ctx:Java8Parser.ResourceContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#primary.
    def enterPrimary(self, ctx:Java8Parser.PrimaryContext):
        statement_text = ctx.getText()
        if "System.console().readLine" in statement_text:
            self.foundInMethodBody.add("readLine")

        if "Integer.parseInt" in statement_text or "Double.parseDouble" in statement_text:
            self.foundInMethodBody.add("TypeChange")

        if "args" in statement_text:
            self.foundInMethodBody.add("args")

        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#primaryNoNewArray.
    def enterPrimaryNoNewArray(self, ctx:Java8Parser.PrimaryNoNewArrayContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#classInstanceCreationExpression.
    def enterClassInstanceCreationExpression(self, ctx:Java8Parser.ClassInstanceCreationExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#typeArgumentsOrDiamond.
    def enterTypeArgumentsOrDiamond(self, ctx:Java8Parser.TypeArgumentsOrDiamondContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#fieldAccess.
    def enterFieldAccess(self, ctx:Java8Parser.FieldAccessContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#arrayAccess.
    def enterArrayAccess(self, ctx:Java8Parser.ArrayAccessContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#methodInvocation.
    def enterMethodInvocation(self, ctx:Java8Parser.MethodInvocationContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#methodInvocation_lf_primary.
    def enterMethodInvocation_lf_primary(self, ctx:Java8Parser.MethodInvocation_lf_primaryContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#methodInvocation_lfno_primary.
    def enterMethodInvocation_lfno_primary(self, ctx:Java8Parser.MethodInvocation_lfno_primaryContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])
        
    # Enter a parse tree produced by Java8Parser#argumentList.
    def enterArgumentList(self, ctx:Java8Parser.ArgumentListContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#methodReference.
    def enterMethodReference(self, ctx:Java8Parser.MethodReferenceContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#methodReference_lf_primary.
    def enterMethodReference_lf_primary(self, ctx:Java8Parser.MethodReference_lf_primaryContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#methodReference_lfno_primary.
    def enterMethodReference_lfno_primary(self, ctx:Java8Parser.MethodReference_lfno_primaryContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#arrayCreationExpression.
    def enterArrayCreationExpression(self, ctx:Java8Parser.ArrayCreationExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#dimExprs.
    def enterDimExprs(self, ctx:Java8Parser.DimExprsContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#dimExpr.
    def enterDimExpr(self, ctx:Java8Parser.DimExprContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#constantExpression.
    def enterConstantExpression(self, ctx:Java8Parser.ConstantExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#expression.
    def enterExpression(self, ctx:Java8Parser.ExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#lambdaExpression.
    def enterLambdaExpression(self, ctx:Java8Parser.LambdaExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#lambdaParameters.
    def enterLambdaParameters(self, ctx:Java8Parser.LambdaParametersContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#inferredFormalParameterList.
    def enterInferredFormalParameterList(self, ctx:Java8Parser.InferredFormalParameterListContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#lambdaBody.
    def enterLambdaBody(self, ctx:Java8Parser.LambdaBodyContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:Java8Parser.AssignmentExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#assignment.
    def enterAssignment(self, ctx:Java8Parser.AssignmentContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#leftHandSide.
    def enterLeftHandSide(self, ctx:Java8Parser.LeftHandSideContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:Java8Parser.AssignmentOperatorContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#conditionalExpression.
    def enterConditionalExpression(self, ctx:Java8Parser.ConditionalExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#conditionalOrExpression.
    def enterConditionalOrExpression(self, ctx:Java8Parser.ConditionalOrExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#conditionalAndExpression.
    def enterConditionalAndExpression(self, ctx:Java8Parser.ConditionalAndExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:Java8Parser.InclusiveOrExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:Java8Parser.ExclusiveOrExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#andExpression.
    def enterAndExpression(self, ctx:Java8Parser.AndExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#equalityExpression.
    def enterEqualityExpression(self, ctx:Java8Parser.EqualityExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#relationalExpression.
    def enterRelationalExpression(self, ctx:Java8Parser.RelationalExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#shiftExpression.
    def enterShiftExpression(self, ctx:Java8Parser.ShiftExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#additiveExpression.
    def enterAdditiveExpression(self, ctx:Java8Parser.AdditiveExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:Java8Parser.MultiplicativeExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#unaryExpression.
    def enterUnaryExpression(self, ctx:Java8Parser.UnaryExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#preIncrementExpression.
    def enterPreIncrementExpression(self, ctx:Java8Parser.PreIncrementExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#preDecrementExpression.
    def enterPreDecrementExpression(self, ctx:Java8Parser.PreDecrementExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#unaryExpressionNotPlusMinus.
    def enterUnaryExpressionNotPlusMinus(self, ctx:Java8Parser.UnaryExpressionNotPlusMinusContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#postfixExpression.
    def enterPostfixExpression(self, ctx:Java8Parser.PostfixExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#postIncrementExpression.
    def enterPostIncrementExpression(self, ctx:Java8Parser.PostIncrementExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#postIncrementExpression_lf_postfixExpression.
    def enterPostIncrementExpression_lf_postfixExpression(self, ctx:Java8Parser.PostIncrementExpression_lf_postfixExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#postDecrementExpression.
    def enterPostDecrementExpression(self, ctx:Java8Parser.PostDecrementExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#postDecrementExpression_lf_postfixExpression.
    def enterPostDecrementExpression_lf_postfixExpression(self, ctx:Java8Parser.PostDecrementExpression_lf_postfixExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    # Enter a parse tree produced by Java8Parser#castExpression.
    def enterCastExpression(self, ctx:Java8Parser.CastExpressionContext):
        self.foundInMethodBody.add(Java8Parser.ruleNames[ctx.getRuleIndex()])

    def get_cyclomatic(self):
        return int(self.Cyclomatic/2)+1
    
    def Cyclomatic_clear(self):
        self.Cyclomatic = 0